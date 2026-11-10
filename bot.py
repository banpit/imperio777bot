import html
import json
import os
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

import config

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
# agendado = execução automática | proxima = envia a próxima da fila agora | todas = envia as 3 agora (teste)
MODO = os.environ.get("MODO", "agendado")

API = f"https://api.telegram.org/bot{TOKEN}"
ARQ_ESTADO = "estado.json"
FUSO = ZoneInfo("America/Sao_Paulo")
LIMITE_LEGENDA = 1024


# ---------------------------------------------------------------- estado
def ler_estado():
    try:
        with open(ARQ_ESTADO) as f:
            estado = json.load(f)
    except Exception:
        estado = {}
    estado.setdefault("msgs", {})   # nome da mensagem -> lista de IDs enviados por último
    estado.setdefault("idx", 0)     # próxima mensagem da fila
    return estado


def salvar_estado(estado):
    with open(ARQ_ESTADO, "w") as f:
        json.dump(estado, f, indent=2)


# ---------------------------------------------------------------- telegram
def montar_texto(msg):
    texto = msg["texto"]
    if config.RODAPE_ATIVO and config.RODAPE:
        texto += "\n\n" + config.RODAPE
    return texto


def formatar(texto):
    """Escapa o texto para HTML e transforma **trecho** em negrito (<b>trecho</b>)."""
    seguro = html.escape(texto, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", seguro, flags=re.S)


def sem_negrito(texto):
    """Versão sem formatação (usada se o Telegram recusar o HTML)."""
    return texto.replace("**", "")


def sem_estilo(botoes):
    return [[{k: v for k, v in b.items() if k != "style"} for b in linha] for linha in botoes]


def tem_estilo(botoes):
    return any("style" in b for linha in botoes for b in linha)


def chamar(metodo, dados, arquivo=None):
    url = f"{API}/{metodo}"
    if arquivo:
        with open(arquivo, "rb") as f:
            return requests.post(url, data=dados, files={"photo": f}, timeout=60)
    return requests.post(url, data=dados, timeout=30)


def enviar_um(metodo, dados, botoes=None, arquivo=None):
    """Envia uma mensagem. Se o Telegram recusar a cor dos botões, tenta sem a cor."""
    if botoes:
        dados["reply_markup"] = json.dumps({"inline_keyboard": botoes})
    r = chamar(metodo, dados, arquivo)
    if r.status_code == 400 and "parse entities" in r.text and dados.get("parse_mode"):
        print("Aviso: Telegram recusou o negrito, reenviando sem formatação.")
        dados.pop("parse_mode")
        for campo in ("caption", "text"):
            if campo in dados:
                dados[campo] = html.unescape(re.sub(r"</?b>", "", dados[campo]))
        r = chamar(metodo, dados, arquivo)
    if r.status_code == 400 and botoes and tem_estilo(botoes):
        print("Aviso: Telegram recusou a cor dos botões, reenviando sem cor.")
        dados["reply_markup"] = json.dumps({"inline_keyboard": sem_estilo(botoes)})
        r = chamar(metodo, dados, arquivo)
    if not r.ok:
        raise RuntimeError(f"Telegram respondeu {r.status_code}: {r.text}")
    return r.json()["result"]["message_id"]


def enviar(msg):
    """Envia a mensagem e devolve a lista de IDs criados."""
    bruto = montar_texto(msg)
    texto = formatar(bruto)
    limite_ok = len(sem_negrito(bruto)) <= LIMITE_LEGENDA  # o limite conta só o texto visível
    botoes = msg.get("botoes")
    imagem = msg.get("imagem")
    tem_imagem = bool(imagem) and os.path.exists(imagem)
    if imagem and not tem_imagem:
        print(f"Aviso: imagem '{imagem}' não encontrada no repositório. Enviando só texto.")

    if tem_imagem and limite_ok:
        return [enviar_um(
            "sendPhoto",
            {"chat_id": CHAT_ID, "caption": texto, "parse_mode": "HTML"},
            botoes,
            imagem,
        )]

    if tem_imagem:
        # texto maior que o limite da legenda: foto sozinha + texto com os botões
        print("Aviso: texto maior que 1024 caracteres, enviando foto e texto separados.")
        id_foto = enviar_um("sendPhoto", {"chat_id": CHAT_ID}, None, imagem)
        id_texto = enviar_um(
            "sendMessage",
            {"chat_id": CHAT_ID, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": True},
            botoes,
        )
        return [id_foto, id_texto]

    return [enviar_um(
        "sendMessage",
        {"chat_id": CHAT_ID, "text": texto, "parse_mode": "HTML", "disable_web_page_preview": True},
        botoes,
    )]


def apagar(msg_id):
    try:
        r = requests.post(
            f"{API}/deleteMessage",
            data={"chat_id": CHAT_ID, "message_id": msg_id},
            timeout=30,
        )
        if r.ok:
            print(f"Apagada a mensagem {msg_id}")
        else:
            print(f"Não consegui apagar {msg_id}: {r.text}")
    except Exception as e:
        print(f"Não consegui apagar {msg_id}: {e}")


# ---------------------------------------------------------------- rotação
def substituir(i, estado):
    """Envia a mensagem i e, só depois, apaga a versão anterior DELA (e de mais nenhuma)."""
    msg = config.MENSAGENS[i]
    nome = msg["nome"]
    novos = enviar(msg)
    antigos = estado["msgs"].get(nome, [])
    estado["msgs"][nome] = novos
    salvar_estado(estado)  # salva já, para não perder o ID se algo falhar depois
    print(f"{nome}: enviada {novos}")
    for antigo in antigos:
        apagar(antigo)


def main():
    nomes = [m["nome"] for m in config.MENSAGENS]
    if len(set(nomes)) != len(nomes):
        sys.exit("Erro: há dois 'nome' repetidos no config.py")

    estado = ler_estado()
    total = len(config.MENSAGENS)
    agora = datetime.now(FUSO)

    if MODO == "todas":
        for i in range(total):
            substituir(i, estado)
        return

    slot = None
    if MODO == "agendado":
        hora_agendada = (agora.hour // 2) * 2  # os envios saem nas horas pares
        slot = agora.strftime("%Y-%m-%d") + f"T{hora_agendada:02d}"
        if config.PAUSA_INICIO <= hora_agendada < config.PAUSA_FIM:
            print(f"Envio das {hora_agendada}h pulado (pausa {config.PAUSA_INICIO}h-{config.PAUSA_FIM}h).")
            return
        if estado.get("ultimo_slot") == slot:
            print(f"O envio das {hora_agendada}h já foi feito hoje. Nada a fazer.")
            return

    i = estado["idx"] % total
    substituir(i, estado)
    estado["idx"] = (i + 1) % total
    if slot:
        estado["ultimo_slot"] = slot
    salvar_estado(estado)


if __name__ == "__main__":
    main()
