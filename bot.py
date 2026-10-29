import os
import json
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# ====== EDITE AQUI ======
IMAGEM = "banner.jpg"

LEGENDA = (
    "<b>Bom dia, pessoal!</b> ☀️\n\n"
    "Confira as novidades de hoje.\n"
    "Toque nos botões abaixo para saber mais."
)

BOTOES = [
    [{"text": "🔗 Acessar o site", "url": "https://exemplo.com"}],
    [
        {"text": "📲 WhatsApp", "url": "https://wa.me/5586999999999"},
        {"text": "📢 Canal", "url": "https://t.me/seucanal"},
    ],
]
# ========================

def enviar_foto():
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    dados = {
        "chat_id": CHAT_ID,
        "caption": LEGENDA,
        "parse_mode": "HTML",
        "reply_markup": json.dumps({"inline_keyboard": BOTOES}),
    }
    with open(IMAGEM, "rb") as foto:
        r = requests.post(url, data=dados, files={"photo": foto}, timeout=60)
    r.raise_for_status()
    print("Mensagem enviada!")

enviar_foto()
