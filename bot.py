import os
import json
import time
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
API = f"https://api.telegram.org/bot{TOKEN}"

# ====== EDITE AQUI ======
IMAGEM = "7cwin.jpg"   # opcional: se o arquivo não existir, envia só texto

TEXTO = (
    "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
    "࿐ 🎰 GRUPO WIN 🎰 ࿐\n\n"
    "🎰 LINK DA PLATAFORMA:\n"
    "↪️ https://7c577.com/?pid=1515197579&fromPage=AGENCY_CENTER\n\n"
    "✅ DEPÓSITO MIN - 5$\n"
    "✅ SAQUE MIN - 10$\n"
    "✅ SEM TAXA DE SAQUE\n"
    "✅ SEM BARRINHA/ROLLOVER\n"
    "🚨 Não crie mais de uma conta na plataforma!\n\n"
    "🔞 Proibido para menores de 18 anos. Jogue com responsabilidade."
)

BOTOES = [[{
    "text": "JOGAR AGORA!",
    "url": "https://7c577.com/?pid=1515197579&fromPage=AGENCY_CENTER",
}]]

INTERVALO = 300             # 5 minutos
DURACAO = 5 * 3600 + 50 * 60  # o loop encerra após 5h50 (limite do GitHub é 6h)
# ========================

ARQ_ID = "ultimo_id.txt"


def enviar():
    markup = json.dumps({"inline_keyboard": BOTOES})
    if os.path.exists(IMAGEM):
        with open(IMAGEM, "rb") as foto:
            r = requests.post(
                f"{API}/sendPhoto",
                data={"chat_id": CHAT_ID, "caption": TEXTO, "reply_markup": markup},
                files={"photo": foto},
                timeout=60,
            )
    else:
        r = requests.post(
            f"{API}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": TEXTO,
                "reply_markup": markup,
                "disable_web_page_preview": True,
            },
            timeout=30,
        )
    r.raise_for_status()
    return r.json()["result"]["message_id"]


def apagar(msg_id):
    try:
        requests.post(
            f"{API}/deleteMessage",
            data={"chat_id": CHAT_ID, "message_id": msg_id},
            timeout=30,
        )
    except Exception as e:
        print("Não consegui apagar:", e)


def ler_id():
    try:
        with open(ARQ_ID) as f:
            return int(f.read().strip())
    except Exception:
        return None


def salvar_id(msg_id):
    with open(ARQ_ID, "w") as f:
        f.write(str(msg_id))


inicio = time.time()
n = 0
while time.time() - inicio < DURACAO:
    anterior = ler_id()
    try:
        novo = enviar()
        if anterior:
            apagar(anterior)
        salvar_id(novo)
        print(f"Ciclo {n}: enviada {novo}, apagada {anterior}")
    except Exception as e:
        print("Erro no ciclo:", e)
    n += 1
    time.sleep(max(0, inicio + n * INTERVALO - time.time()))
