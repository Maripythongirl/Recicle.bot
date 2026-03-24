import discord
import random
from discord.ext import commands
from videoart import videos
from dados import itens
from lugar import categorias
#CONFIG
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

#EVENTO 
@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

# COMANDOS
@bot.command()
async def tedio(ctx):
    video = random.choice(videos)
    await ctx.send(f"""🎨 **Ideia de artesanato aleatória**
📺 YouTube:
{video['youtube']}
🎵 TikTok:
{video['tiktok']}
🧰 Material usado:
{video['material']}
""")

@bot.command()
async def ajuda(ctx):
    await ctx.send("""
♻️ Como usar o bot:
Comandos:

-Digite: !reciclagem
-Informe uma das opções de categorias
-Informe o material
-O bot dirá se o material é ou não reciclável, como descartar, sua categoria e um vídeo de artesanato para a reciclagem do objeto.
                   
-Digite: !ajuda
-Aparecerá esta descrição de como o bot funciona.

-Digite: !tedio
-Aparecerá um dos vídeos base de forma aleatória de artesanato com materiais recicláveis como recomendação para fazer no tempo livre.
O bot vai te orientar sobre descarte e reutilização 🌱
""")

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

        # SE FOR CATEGORIA 
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

        # ITEM DIRETO
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

        # NÃO RECONHECIDO
        else:
            await ctx.send("""
❓ Não reconheci esse item.""")

    except:
        await ctx.send("⏳ Tempo esgotado! Use !reciclagem novamente.")

bot.run("seu token")
