# =====================================================================
#  CONFIGURAÇÕES DO BOT
#  É AQUI que você edita textos, links, imagens, botões e a pausa.
#  Não precisa mexer no bot.py.
# =====================================================================

# ---------- LINKS ----------
LINK_7J = "https://7jwin.vip/?pid=3791782603&fromPage=AGENCY_CENTER"
LINK_7C = "https://7c577.com/?pid=1515197579&fromPage=AGENCY_CENTER"
LINK_POPJUN = "https://22popjun.com/?a=70Oa0m&pkgCode=popjun-011&from=1001"
LINK_ID = "https://t.me/imperio777ofc"

# ---------- RODAPÉ (entra no fim de todas as mensagens) ----------
RODAPE_ATIVO = True
RODAPE = "🔞 Proibido para menores de 18 anos. Jogue com responsabilidade."

# ---------- PAUSA (horário de Brasília) ----------
# Os envios saem nas horas pares (0h, 2h, 4h, 6h...).
# O envio das horas que caem de PAUSA_INICIO até antes de PAUSA_FIM é pulado.
# Com 3 e 6: o envio das 4h é pulado; o das 2h e o das 6h acontecem normalmente.
# Para desligar a pausa, use PAUSA_INICIO = 0 e PAUSA_FIM = 0.
PAUSA_INICIO = 3
PAUSA_FIM = 6

# ---------- MENSAGENS (enviadas em rotação: 1, 2, 3, 1, 2, 3...) ----------
# "nome":   identificador único (não repita e não mude depois de em uso)
# "imagem": nome do arquivo no repositório (se não existir, envia só texto)
# "botoes": cada item da lista é UMA LINHA de botões
#           "style": "primary" = azul | "success" = verde | "danger" = vermelho
#           sem "style" = cor padrão do Telegram
MENSAGENS = [
    {
        "nome": "m1",
        "imagem": "imperio777sorteio.jpg",
        "texto": (
            "SORTEIO DE 300$ NO PIX 🍀\n"
            "2 PIX DE 150$ (2 GANHADORES) 📌\n"
            "PLATAFORMAS VALIDAS PARA PARTICIPAR DO SORTEIO ⤵\n\n"
            "🎰 7JWIN:\n"
            f"{LINK_7J}\n\n"
            "🎰 7CWIN:\n"
            f"{LINK_7C}\n\n"
            "🎰 POPJUN:\n"
            f"{LINK_POPJUN}\n\n"
            "QUALQUER VALOR DE DEPÓSITO E VÁLIDO PARA PARTICIPAR! ✅\n\n"
            "❗ Observação: Fazendo conta nas 3 plataformas poderá escolher 3 números para o sorteio!"
        ),
        "botoes": [
            [{"text": "JOGAR NA 7JWIN", "url": LINK_7J}],
            [{"text": "JOGAR NA 7CWIN", "url": LINK_7C}],
            [{"text": "JOGAR NA POPJUN", "url": LINK_POPJUN}],
            [{"text": "🟡 ENVIAR 🆔 PARA SORTEIO", "url": LINK_ID, "style": "primary"}],
        ],
    },
    {
        "nome": "m2",
        "imagem": "7jwin.jpeg",
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO WIN 🎰 ࿐\n\n"
            "🎰 LINK DA PLATAFORMA:\n"
            f"↪️ {LINK_7J}\n\n"
            "✅ DEPÓSITO MIN - 5$\n"
            "✅ SAQUE MIN - 10$\n"
            "✅ SEM TAXA DE SAQUE\n"
            "✅ SEM BARRINHA/ROLLOVER\n"
            "🚨 Não crie mais de uma conta na plataforma!"
        ),
        "botoes": [
            [{"text": "JOGAR NA 7JWIN", "url": LINK_7J, "style": "primary"}],
        ],
    },
    {
        "nome": "m3",
        "imagem": "7cwin.jpg",
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO WIN 🎰 ࿐\n\n"
            "🎰 LINK DA PLATAFORMA:\n"
            f"{LINK_7C}\n\n"
            "✅ DEPÓSITO MIN - 5$\n"
            "✅ SAQUE MIN - 10$\n"
            "✅ SEM TAXA DE SAQUE\n"
            "✅ SEM BARRINHA/ROLLOVER\n"
            "🚨 Não crie mais de uma conta na plataforma!"
        ),
        "botoes": [
            [{"text": "JOGAR NA 7CWIN", "url": LINK_7C, "style": "primary"}],
        ],
    },
]
