# =====================================================================
#  CONFIGURAÇÕES DO BOT
#  É AQUI que você edita textos, links, imagens, botões e a pausa.
#  Não precisa mexer no bot.py.
#
#  NEGRITO: coloque o trecho entre *asteriscos*  (ou **dois asteriscos**).
#           Ex.: *SORTEIO DE 400$*   (só funciona dentro da mesma linha com 1 asterisco)
# =====================================================================

# ---------- LINKS ----------
# Sorteio (mensagem 1)
LINK_OJ_789 = "https://ojwin789.com/?id=736514927"
LINK_POPGLD_33 = "https://33popgld.com?a=42cOsF&pkgCode=popgld-011&from=1001"
LINK_754_WWW = "https://lfcoqueiro.com/?id=405095043"
LINK_ID = "https://t.me/imperio777ofc"

# OJWIN (mensagem 2)
LINK_OJ = "https://ojwin.com/?id=736514927"
LINK_OJ_ALT = "https://ojwinyundun3.com/?id=736514927"

# POPGLD (mensagem 3)
LINK_POP = "https://www.popgld.com/?a=42cOsF&pkgCode=popgld-011&from=1001"
LINK_POP_ALT = "https://33popgld.com/?a=42cOsF&pkgCode=popgld-011&from=1001"

# 754WIN (mensagem 4)
LINK_754 = "https://lfcoqueiro.com/?id=405095043"
LINK_754_ALT = "https://www.lf-coqueiro.com/?id=405095043"

# 7JWIN (mensagem 5)
LINK_7J = "https://7jwin.vip/?pid=3791782603&fromPage=AGENCY_CENTER"
LINK_7J_ALT = "https://7j8888.com/?pid=3791782603&fromPage=AGENCY_CENTER"

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

# ---------- MENSAGENS (enviadas em rotação: 1, 2, 3, 4, 5, 1, 2...) ----------
# "nome":   identificador único (não repita e não mude depois de em uso)
# "imagem": nome do arquivo no repositório (se não existir, envia só texto)
# "botoes": cada item da lista é UMA LINHA de botões
#           "style": "primary" = azul | "success" = verde | "danger" = vermelho
#           sem "style" = cor padrão do Telegram
MENSAGENS = [
    # ---------------------------------------------------------------- 1
    {
        "nome": "m1",
        "imagem": "sorteiopix.jpg",
        "texto": (
            "🍀 *SORTEIO DE 400$ NO PIX*\n"
            "2 PIX DE 200$ (2 GANHADORES)\n\n"
            "*QUALQUER VALOR DE DEPÓSITO É VÁLIDO PARA PARTICIPAR!* ✅\n"
            "PLATAFORMAS VÁLIDAS PARA O SORTEIO ⤵️\n\n"
            "🎰 *OJWIN:*\n"
            f"{LINK_OJ_789}\n\n"
            "🎰 *POPGLD:*\n"
            f"{LINK_POPGLD_33}\n\n"
            "🎰 *754WIN:*\n"
            f"{LINK_754_WWW}\n\n"
            "❗ Obs. Fazendo conta nas 3 plataformas e depositando, pode escolher 3 números.\n\n"
            "📆 *Data do sorteio: (29/11)*"
        ),
        "botoes": [
            [{"text": "🎰 JOGAR NA OJWIN", "url": LINK_OJ_789}],
            [{"text": "🎰 JOGAR NA POPGLD", "url": LINK_POPGLD_33}],
            [{"text": "🎰 JOGAR NA 754WIN", "url": LINK_754_WWW}],
            [{"text": "ENVIAR 🆔 PARA PARTICIPAR", "url": LINK_ID, "style": "primary"}],
        ],
    },
    # ---------------------------------------------------------------- 2
    {
        "nome": "m2",
        "imagem": "ojwin.jpg",
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO WIN 🎰 ࿐\n\n"
            "🎰 *LINK DA PLATAFORMA:*\n"
            f"{LINK_OJ}\n\n"
            "🔗 *LINK ALTERNATIVO:*\n"
            f"{LINK_OJ_ALT}\n\n"
            "✅ *DEPÓSITO MIN - 10$*\n"
            "✅ *SAQUE MIN - 10$*\n"
            "✅ *SEM TAXA DE SAQUE*\n"
            "✅ *SEM BARRINHA/ROLLOVER*\n"
            "🚨 *Não crie mais de uma conta na plataforma!*"
        ),
        "botoes": [
            [{"text": "🎰 JOGAR NA OJWIN", "url": LINK_OJ}],
            [{"text": "🔗 LINK ALTERNATIVO", "url": LINK_OJ_ALT}],
        ],
    },
    # ---------------------------------------------------------------- 3
    {
        "nome": "m3",
        "imagem": "popgld.jpg",
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO POP 🎰 ࿐\n\n"
            "🎰 *LINK DA PLATAFORMA:*\n"
            f"{LINK_POP}\n\n"
            "🔗 *LINK ALTERNATIVO:*\n"
            f"{LINK_POP_ALT}\n\n"
            "✅ *DEPÓSITO MIN - 10$*\n"
            "✅ *SAQUE MIN - 20$*\n"
            "✅ *SEM TAXA DE SAQUE*\n"
            "✅ *SEM BARRINHA/ROLLOVER*\n"
            "🚨 *Não crie mais de uma conta na plataforma!*"
        ),
        "botoes": [
            [{"text": "🎰 JOGAR NA POPGLD", "url": LINK_POP}],
            [{"text": "🔗 LINK ALTERNATIVO", "url": LINK_POP_ALT}],
        ],
    },
    # ---------------------------------------------------------------- 4 (nova)
    {
        "nome": "m4",
        "imagem": "lfcoqueiro.jpg",
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO LF 🎰 ࿐\n\n"
            "🎰 *LINK DA PLATAFORMA:*\n"
            f"{LINK_754}\n\n"
            "🔗 *LINK ALTERNATIVO:*\n"
            f"{LINK_754_ALT}\n\n"
            "✅ *DEPÓSITO MIN - 10$*\n"
            "✅ *SAQUE MIN - 10$*\n"
            "✅ *SEM TAXA DE SAQUE*\n"
            "✅ *SEM BARRINHA/ROLLOVER*\n"
            "🚨 *Não crie mais de uma conta na plataforma!*"
        ),
        "botoes": [
            [{"text": "🎰 JOGAR NA LF-COQUEIRO", "url": LINK_754}],
            [{"text": "🔗 LINK ALTERNATIVO", "url": LINK_754_ALT}],
        ],
    },
    # ---------------------------------------------------------------- 5 (nova)
    {
        "nome": "m5",
        "imagem": "7jwin.jpg",
        "texto": (
            "🇱 🇦 🇳 🇨 🇦 🇲 🇪 🇳 🇹 🇴\n"
            "࿐ 🎰 GRUPO WIN 🎰 ࿐\n\n"
            "🎰 *LINK DA PLATAFORMA:*\n"
            f"{LINK_7J}\n\n"
            "🔗 *LINK ALTERNATIVO:*\n"
            f"{LINK_7J_ALT}\n\n"
            "✅ *DEPÓSITO MIN - 5$*\n"
            "✅ *SAQUE MIN - 10$*\n"
            "✅ *SEM TAXA DE SAQUE*\n"
            "✅ *SEM BARRINHA/ROLLOVER*\n"
            "🚨 *Não crie mais de uma conta na plataforma!*"
        ),
        "botoes": [
            [{"text": "🎰 JOGAR NA 7JWIN", "url": LINK_7J}],
            [{"text": "🔗 LINK ALTERNATIVO", "url": LINK_7J_ALT}],
        ],
    },
]
