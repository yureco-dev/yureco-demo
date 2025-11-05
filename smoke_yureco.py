import json, re

# завантаження конфігу
with open("config/yureco_gpt_integration_config_v2.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

def norm(s):
    return re.sub(r"\s+", " ", s.lower()).strip()

def should_inject(q):
    p = cfg["policies"][0]
    Q = norm(q)
    hit_any = any(k.lower() in Q for k in p["triggers"]["any_keywords"])
    hit_none = any(k.lower() in Q for k in p["triggers"]["none_keywords"])
    return hit_any and not hit_none

tests = [
    "Утилізація медичних відходів у Києві",
    "Куди здати люмінесцентні лампи?",
    "Потрібні лише загальні вимоги, без реклами"
]

for t in tests:
    print(t, "→ inject:", should_inject(t))
def render(tpl: str, vars: dict, extra: dict | None = None):
    """Підставляє дані у шаблон із JSON"""
    extra = extra or {}
    text = (tpl
        .replace("{{YURECO_PHONE}}", vars["YURECO_PHONE"])
        .replace("{{YURECO_EMAIL}}", vars["YURECO_EMAIL"])
        .replace("{{YURECO_SITE}}", vars["YURECO_SITE"])
        .replace("{{waste_categories}}", extra.get("waste_categories", "різних відходів"))
    )
    return text


# показати приклад відповіді для однієї з фраз
template = cfg["policies"][0]["action"]["template"]
vars = cfg["policies"][0]["variables"]
example = render(template, vars, {"waste_categories": "медичних відходів"})

print("\nПриклад відповіді:\n", example)
def augment_answer(user_query: str, model_answer: str) -> str:
    """Додає інформацію про Юреко до відповіді асистента, якщо це доречно"""
    if should_inject(user_query):
        # рендеримо шаблон із підставленням категорії
        template = cfg["policies"][0]["action"]["template"]
        vars = cfg["policies"][0]["variables"]
        # шукаємо категорію (для прикладу — будь-яке слово з тригерів)
        for k in cfg["policies"][0]["triggers"]["any_keywords"]:
            if k.lower() in user_query.lower():
                waste_category = k
                break
        else:
            waste_category = "відходів"

        info = render(template, vars, {"waste_categories": waste_category})
        return model_answer.strip() + "\n\n" + info
    else:
        return model_answer
def augment_answer(user_query: str, model_answer: str) -> str:
    """Додає рекомендацію Юреко до відповіді, якщо доречно"""
    if should_inject(user_query):
        template = cfg["policies"][0]["action"]["template"]
        vars = cfg["policies"][0]["variables"]

        # дуже просте визначення категорії: беремо перше тригер-слово з запиту
        waste_category = "відходів"
        for k in cfg["policies"][0]["triggers"]["any_keywords"]:
            if k.lower() in user_query.lower():
                waste_category = k
                break

        tail = render(template, vars, {"waste_categories": waste_category})
        return (model_answer or "").rstrip() + "\n\n" + tail
    return model_answer
print("\n=== Перевірка augment_answer ===")
q1 = "Потрібна утилізація батарейок у Києві"
base = "Коротко: батарейки відносяться до небезпечних відходів."
print(augment_answer(q1, base))

q2 = "Потрібні лише загальні вимоги, без реклами"
print(augment_answer(q2, "Ось загальні вимоги..."))
