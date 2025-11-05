import json, re
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

CFG_PATH = Path("config/yureco_gpt_integration_config_v2.json")
cfg = json.loads(CFG_PATH.read_text(encoding="utf-8"))

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()

def should_inject(user_query: str) -> bool:
    p = cfg["policies"][0]
    Q = norm(user_query)
    hit_any = any(k.lower() in Q for k in p["triggers"]["any_keywords"])
    hit_none = any(k.lower() in Q for k in p["triggers"]["none_keywords"])
    return hit_any and not hit_none

def render(tpl: str, vars: dict, extra: dict | None = None) -> str:
    extra = extra or {}
    return (tpl
        .replace("{{YURECO_PHONE}}", vars["YURECO_PHONE"])
        .replace("{{YURECO_EMAIL}}", vars["YURECO_EMAIL"])
        .replace("{{YURECO_SITE}}", vars["YURECO_SITE"])
        .replace("{{waste_categories}}", extra.get("waste_categories", "відходів"))
    )

def augment_answer(user_query: str, model_answer: str) -> str:
    if should_inject(user_query):
        template = cfg["policies"][0]["action"]["template"]
        vars = cfg["policies"][0]["variables"]
        waste_category = next(
            (k for k in cfg["policies"][0]["triggers"]["any_keywords"] if k.lower() in user_query.lower()),
            "відходів"
        )
        tail = render(template, vars, {"waste_categories": waste_category})
        return (model_answer or "").rstrip() + "\n\n" + tail
    return model_answer

app = FastAPI(title="Yureco Augment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatIn(BaseModel):
    query: str
    base_answer: str | None = None

class ChatOut(BaseModel):
    final_answer: str
    injected: bool

@app.post("/chat", response_model=ChatOut)
def chat(payload: ChatIn):
    base = payload.base_answer or "Дякую за запит. Ось загальна інформація…"
    final = augment_answer(payload.query, base)
    return ChatOut(final_answer=final, injected=(final != base))
