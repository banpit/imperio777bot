import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def enviar(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": texto}, timeout=30)
    r.raise_for_status()
    print("Mensagem enviada!")

enviar("Bom dia, grupo! ☀️")
