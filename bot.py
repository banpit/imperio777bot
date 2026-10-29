import os
import json
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
API = f"https://api.telegram.org/bot{TOKEN}"

# ================== EDITE AQUI ==================
LINK_7C = "https://7c577.com/?pid=1515197579&fromPage=AGENCY_CENTER"
LINK_POPJUN = "https://22popjun.com/?a=70Oa0m&pkgCode=popjun-011&from=1001"
LINK_ID = "https://t.me/imperio777ofc"

MENSAGENS = [
    {
        "nome": "m1",
        "intervalo": 10 * 60,    # mensagem 1: a cada 10 minutos
        "offset": 0,             # nos minutos :00, :10, :20...
        "imagem": "7cwin.jpg",  # opcional: sem o arquivo, envia só texto
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO WIN 🎰 ࿐\n\n"
            "🎰 LINK DA PLATAFORMA:\n"
            f"↪️ {LINK_7C}\n\n"
            "✅ DEPÓSITO MIN - 5$\n"
            "✅ SAQUE MIN - 10$\n"
            "✅ SEM TAXA DE SAQUE\n"
            "✅ SEM BARRINHA/ROLLOVER\n"
            "🚨 Não crie mais de uma conta na plataforma!\n\n"
            "🔞 Proibido para menores de 18 anos. Jogue com responsabilidade."
        ),
        "botoes": [[{"text": "JOGAR AGORA!", "url": LINK_7C}]],
    },
    {
        "nome": "m2",
        "intervalo": 15 * 60,    # mensagem 2: a cada 15 minutos
        "offset": 5 * 60,        # nos minutos :05, :20, :35, :50
        "imagem": "imperio777sorteio.jpg",
        "texto": (
            "SORTEIO DE 300$ NO PIX 🍀\n"
            "2 PIX DE 150$ (2 GANHADORES) 📌\n\n"
            "PLATAFORMAS VALIDAS PARA PARTICIPAR DO SORTEIO ⤵\n\n"
            "🎰 7CWIN:\n"
            f"{LINK_7C}\n"
            "🎰 POPJUN:\n"
            f"{LINK_POPJUN}\n\n"
            "QUALQUER VALOR DE DEPÓSITO E VÁLIDO PARA PARTICIPAR! ✅\n\n"
            "❗ Observação: Fazendo conta nas 2 plataformas poderá escolher 2 números para o sorteio!\n\n"
            "🔞 Proibido para menores de 18 anos. Jogue com responsabilidade."
        ),
        "botoes": [
            [{"text": "🎰 JOGAR NA 7CWIN", "url": LINK_7C}],
            [{"text": "🎰 JOGAR NA POPJUN", "url": LINK_POPJUN}],
            [{"text": "ENVIAR 🆔 PARA O SORTEIO", "url": LINK_ID, "style": "primary"}],
        ],
    },
]

HORA_INICIO = 10                # começa às 10h (Brasília)
HORA_FIM = 23                   # para às 23h (Brasília)
DURACAO = 4 * 3600 + 55 * 60    # cada execução dura ~4h55
TOLERANCIA = 5 * 60             # se atrasar mais que isso, espera o próximo horário
# ================================================

ARQ_ESTADO = "estado.json"
# Execução manual simples = envia as 2 mensagens uma vez e encerra (teste)
MODO_TESTE = os.environ.get("MODO_TESTE", "false") == "true"


def dentro_do_horario():
    hora = datetime.now(ZoneInfo("America/Sao_Paulo")).hour
    return HORA_INICIO <= hora < HORA_FIM


def ler_estado():
    try:
        with open(ARQ_ESTADO) as f:
            return json.load(f)
    except Exception:
        return {}


def salvar_estado(estado):
    with open(ARQ_ESTADO, "w") as f:
        json.dump(estado, f)


def sem_estilo(botoes):
    return [[{k: v for k, v in b.items() if k != "style"} for b in linha] for linha in botoes]


def _post(msg, botoes):
    markup = json.dumps({"inline_keyboard": botoes})
    imagem = msg.get("imagem")
    if imagem and os.path.exists(imagem):
        with open(imagem, "rb") as foto:
            return requests.post(
                f"{API}/sendPhoto",
                data={"chat_id": CHAT_ID, "caption": msg["texto"], "reply_markup": markup},
                files={"photo": foto},
                timeout=60,
            )
    return requests.post(
        f"{API}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg["texto"],
            "reply_markup": markup,
            "disable_web_page_preview": True,
        },
        timeout=30,
    )


def enviar(msg):
    r = _post(msg, msg["botoes"])
    if r.status_code == 400:
        # fallback: tenta de novo sem a cor dos botões
        r = _post(msg, sem_estilo(msg["botoes"]))
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


def processar(msg, estado, agora):
    nome = msg["nome"]
    slot = int((agora - msg["offset"]) // msg["intervalo"])
    inicio_slot = slot * msg["intervalo"] + msg["offset"]

    if not MODO_TESTE:
        if estado.get("slot_" + nome) == slot:
            return  # já enviada neste horário
        if agora - inicio_slot > TOLERANCIA:
            return  # perdeu esse horário, espera o próximo

    try:
        novo = enviar(msg)
        anterior = estado.get("id_" + nome)
        if anterior:
            apagar(anterior)
        estado["id_" + nome] = novo
        estado["slot_" + nome] = slot
        salvar_estado(estado)
        print(f"{nome}: enviada {novo}, apagada {anterior}")
    except Exception as e:
        print(f"{nome}: erro no envio:", e)
        estado["slot_" + nome] = slot  # evita repetir sem parar no mesmo horário


estado = ler_estado()
inicio = time.time()

while True:
    if not MODO_TESTE:
        if not dentro_do_horario():
            print("Fora do horário de envio. Encerrando.")
            break
        if time.time() - inicio >= DURACAO:
            print("Fim desta execução.")
            break

    agora = time.time()
    for m in MENSAGENS:
        processar(m, estado, agora)
        time.sleep(1)

    if MODO_TESTE:
        break
    time.sleep(15)
