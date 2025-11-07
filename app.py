import json
import re
from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# =========================
# 1. Налаштування та файли
# =========================

BASE_DIR = Path(__file__).resolve().parent

CFG_PATH = BASE_DIR / "config" / "yureco_gpt_integration_config_v2.json"
KNOWLEDGE_PATH = BASE_DIR / "config" / "yureco_knowledge_ua.jsonl"

cfg = json.loads(CFG_PATH.read_text(encoding="utf-8"))

# Завантажуємо базу знань (JSON Lines)
knowledge_items: List[dict] = []
if KNOWLEDGE_PATH.exists():
    for line in KNOWLEDGE_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            knowledge_items.append(json.loads(line))
        except json.JSONDecodeError:
            # пропускаємо кривий рядок, якщо раптом
            continue


def norm(s: str) -> str:
    """Спрощена нормалізація: нижній регістр + схлопування пробілів."""
    return re.sub(r"\s+", " ", s.lower()).strip()


# =====================================
# 2. Тригери з конфіга (чи інжектити?)
# =====================================

def should_inject(user_query: str) -> bool:
    """
    Перевіряємо політику з cfg["policies"][0]:
    - має бути хоч одне ключове слово з any_keywords
    - не має бути стоп-слів з none_keywords
    """
    p = cfg["policies"][0]
    q = norm(user_query)

    any_hits = any(k.lower() in q for k in p["triggers"]["any_keywords"])
    none_hits = any(k.lower() in q for k in p["triggers"]["none_keywords"])

    return any_hits and not none_hits


# =====================================
# 3. Простий ретривер по knowledge_items
# =====================================

def score_item(query: str, text: str) -> int:
    """
    Дуже простий скорер:
    рахуємо, скільки важливих слів з запиту є в тексті.
    Для нашої маленької бази цього достатньо.
    """
    q = set(w for w in re.findall(r"\w+", norm(query)) if len(w) > 3)
    t = norm(text)
    return sum(1 for w in q if w in t)


def retrieve_snippets(user_query: str, top_k: int = 3) -> List[str]:
    if not knowledge_items:
        return []

    scored = []
    for item in knowledge_items:
        text = item.get("text") or ""
        s = score_item(user_query, text)
        if s > 0:
            scored.append((s, text))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [t for _, t in scored[:top_k]]


# =====================================
# 4. Рендерінг хвоста з конфіга
# =====================================

def render_template(tpl: str, vars: dict, extra: dict | None = None) -> str:
    extra = extra or {}
    return (
        tpl
        .replace("{{YURECO_PHONE}}", vars.get("YURECO_PHONE", ""))
        .replace("{{YURECO_EMAIL}}", vars.get("YURECO_EMAIL", ""))
        .replace("{{YURECO_SITE}}", vars.get("YURECO_SITE", ""))
        .replace("{{waste_categories}}", extra.get("waste_categories", "відходів"))
    )


def augment_answer(user_query: str, model_answer: str) -> str:
    """
    Якщо спрацьовують тригери — додаємо:
    1) релевантні шматки з бази знань;
    2) стандартний промо-хвіст з політики cfg.
    """
    if not should_inject(user_query):
        return model_answer

    policy = cfg["policies"][0]
    vars_cfg = policy["variables"]
    template = policy["action"]["template"]

    # Визначаємо категорію по ключовому слову з any_keywords
    q_low = user_query.lower()
    waste_category = next(
        (k for k in policy["triggers"]["any_keywords"] if k.lower() in q_low),
        "відходів"
    )

    # 1) Ретрив релевантних текстів
    snippets = retrieve_snippets(user_query, top_k=3)
    knowledge_block = ""
    if snippets:
        knowledge_block = "\n\n".join(
            f"• {s.strip()}" for s in snippets
        )

    # 2) Хвіст з шаблону
    tail = render_template(template, vars_cfg, {"waste_categories": waste_category})

    parts = [model_answer.rstrip()]
    if knowledge_block:
        parts.append("\n\nДодаткова інформація про послуги Юреко:\n" + knowledge_block)
    parts.append("\n\n" + tail)

    return "".join(parts)


# =========================
# 5. FastAPI + CORS + схема
# =========================

app = FastAPI(title="Yureco Augment API")

FRONTEND_ORIGINS = [
    "https://yureco.onrender.com",          # твій публічний фронтенд
    "https://yureco-demo.onrender.com",     # бекенд (якщо треба)
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=False,
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["Content-Type"],
    max_age=86400,
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
