import discord
from discord.ext import commands

# ===== CONFIG =====

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== BANCO DE ITENS =====
itens = {
    #plastico
    "garrafa pet": {
        "reciclavel": True,
        "categoria": "plástico",
        "descarte": "Lavar, amassar e descartar no reciclável.",
        "video": {
            "youtube": "https://youtube.com/shorts/C7ykJfepVqg?si=B_eIYPtCnVr5D2-g",
            "tiktok": "https://vt.tiktok.com/ZSuWTdE2L/"
        }
    },
    "tampinha": {
        "reciclavel": True,
        "categoria": "plástico",
        "descarte": "Limpar, secar e descartar no lixo reciclável.",
        "video": {
            "youtube": "https://youtube.com/shorts/4L5o9pXlLEU?si=lmtclKI26FPX6q0E",
            "tiktok": "https://vt.tiktok.com/ZSuWEdQTL/"
        }
    },
    "pote de margarina": {
        "reciclavel": True,
        "categoria": "plástico",
        "descarte": "Lavar antes de descartar.",
        "video": {
            "youtube": "https://youtu.be/uZc3gfQrvww?si=LCJg1cbS255a4jiJ",
            "tiktok": "https://vt.tiktok.com/ZSuW3vuWk/"}
                    },
    #papel
    "papel": {
        "reciclavel": True,
        "categoria": "papel",
        "descarte": "Manter seco.",
        "video": {
            "youtube": "https://youtube.com/shorts/G3N2XyauZGk?si=6zC0IqKXZiAlEeOV",
            "tiktok": "https://vt.tiktok.com/ZSuWT3Ty5/"
        }
    },
    #metal
    "lata de aluminio": {
        "reciclavel": True,
        "categoria": "metal",
        "descarte": "Lavar e amassar.",
        "video": {
            "youtube": "https://youtu.be/VtZBr3Z1F9k?si=WXYxQikysnsbrZ9M",
            "tiktok": "https://vt.tiktok.com/ZSuWw3TVX/"
        }
    },
    "tampinha": {
        "reciclavel": True,
        "categoria": "metal",
        "descarte": "Limpar e descartar no lixo reciclável.",
        "video": {
            "youtube": "https://youtu.be/BpyadBGgj38?si=iunWXO_lcadBlxqZ",
            "tiktok": "https://vt.tiktok.com/ZSuWEUgea/"
        }
    },
    "lacre": {
        "reciclavel": True,
        "categoria": "metal",
        "descarte": "Limpar e descartar no lixo reciclável.",
        "video": {
            "youtube": "https://youtube.com/shorts/T7TMzE7BjMA?si=bM91VJys51HBtfsv",
            "tiktok": "https://vt.tiktok.com/ZSuWETHUL/"
        }
    },
    #vidro
    "garrafa de vidro": {
        "reciclavel": True,
        "categoria": "vidro",
        "descarte": "Descartar com cuidado.",
        "video": {
            "youtube": "https://youtube.com/shorts/l71ZnQqcNa8?si=1_XDRo-Xe7fbr001",
            "tiktok": "https://vt.tiktok.com/ZSuWKBv9L/"
        }
    },
    #eletrônico
    "pilha": {
        "reciclavel": False,
        "categoria": "especial",
        "descarte": "Levar a pontos de coleta.",
        "video": None
    },
    "lâmpada": {
        "reciclavel": False,
        "categoria": "especial",
        "descarte": "Levar a coleta específica.",
        "video": None
    },
    "bituca de cigarro": {
        "reciclavel": False,
        "categoria": "lixo comum",
        "descarte": "Lixo comum.",
        "video": None
    },
    "resto de comida": {
        "reciclavel": False,
        "categoria": "orgânico",
        "descarte": "Lixo orgânico.",
        "video": None
    }
}

# ===== CATEGORIAS =====
categorias = {
    "plástico": [i for i in itens if itens[i]["categoria"] == "plástico"],
    "papel": [i for i in itens if itens[i]["categoria"] == "papel"],
    "vidro": [i for i in itens if itens[i]["categoria"] == "vidro"],
    "metal": [i for i in itens if itens[i]["categoria"] == "metal"],
    "especial": [i for i in itens if itens[i]["categoria"] == "especial"],
    "orgânico": [i for i in itens if itens[i]["categoria"] == "orgânico"],
    "lixo comum": [i for i in itens if itens[i]["categoria"] == "lixo comum"]
}
# ===== EVENTO =====
@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

# ===== COMANDO PRINCIPAL =====
@bot.command()
async def reciclagem(ctx):

    await ctx.send("""
♻️ O que você quer reciclar?

Sugestões:
🧴 plástico
📄 papel
🍾 vidro
🥫 metal
🔋 pilha
                   
Aqui alugns não recicláveis:
🚮 lixo comum
🌱 orgânico
""")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        # PRIMEIRA RESPOSTA
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        obj = msg.content.lower()

        # ===== SE FOR CATEGORIA =====
        if obj in categorias:
            lista = categorias[obj]
            texto = "\n".join([f"- {i}" for i in lista])

            await ctx.send(f"""
📦 Categoria: {obj}

Exemplos:
{texto}

Digite um item específico 😉
""")

            try:
                # SEGUNDA RESPOSTA
                msg2 = await bot.wait_for("message", timeout=30.0, check=check)
                obj2 = msg2.content.lower()

                if obj2 in itens:
                    item = itens[obj2]

                    if item["reciclavel"]:
                        await ctx.send(f"""
♻️ **{obj2.upper()} é reciclável!**

📦 Categoria: {item['categoria']}

🗑️ Descarte:
{item['descarte']}

🎨 Ideias:
📺 {item['video']['youtube']}
🎵 {item['video']['tiktok']}

🌱 Dica: quanto mais limpo, melhor!
""")
                    else:
                        await ctx.send(f"""
❌ **{obj2.upper()} não é reciclável**

🗑️ Descarte:
{item['descarte']}
""")
                else:
                    await ctx.send("❓ Item não reconhecido.")

            except:
                await ctx.send("⏳ Tempo esgotado na segunda resposta.")

        # ===== SE FOR ITEM DIRETO =====
        elif obj in itens:
            item = itens[obj]

            if item["reciclavel"]:
                await ctx.send(f"""
♻️ **{obj.upper()} é reciclável!**

📦 Categoria: {item['categoria']}

🗑️ Descarte:
{item['descarte']}

🎨 Ideias:
📺 {item['video']['youtube']}
🎵 {item['video']['tiktok']}

🌱 Dica: quanto mais limpo, melhor!
""")
            else:
                await ctx.send(f"""
❌ **{obj.upper()} não é reciclável**

🗑️ Descarte:
{item['descarte']}
""")

        # ===== NÃO RECONHECIDO =====
        else:
            await ctx.send("""
❓ Não reconheci esse item.""")

    except:
        await ctx.send("⏳ Tempo esgotado! Use !reciclagem novamente.")

# ===== START =====
bot.run("seu token")
