import discord
from discord.ext import commands
import random
import os
import requests
#from model import get_class
import webserver   

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'sigo vivo kbrones, yo soy {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("je" * count_heh)

@bot.command()
async def number(ctx):
    await ctx.send(random.randint(0,100))

@bot.command()
async def coin(ctx):
    dolar=["escudo", "corona"]
    await ctx.send("se ha lanzado la moneda:"),
    await ctx.send(f'ha salido ' + random.choice(dolar))

ans= ["jajajaja", "jajsajsjaajjs", "que buen meme", "XD"]

@bot.command()
async def meme(ctx):
    imagenes= (os.listdir('img'))
    with open(f'img/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    await ctx.send(random.choice(ans))

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("1025 pokemons y no puedes darme uno que exista")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Cual de todos?")

@bot.command()
async def game(ctx):
    an = random.randint(0,10)
    bn = random.randint(0,10)
    await ctx.send("¡Juguemos!"),
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
            if response.content in [an + bn]:
                await ctx.send("respusta correcta")
            else:
                await ctx.send('no imbecil, es', an + bn)

@bot.command()
async def clean(ctx):
    await ctx.channel.purge()
    await ctx.send("Todo listo Jefe", delete_after = 3)

#@bot.command()
#async def check(ctx):
#    if ctx.message.attachments:
#        for attachment in ctx.message.attachments:
#            file_name = attachment.filename
#            file_url = attachment.url
#            await attachment.save(f"./{attachment.filename}")
#            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
#    else:
#        await ctx.send("con que imagen imbecil?")

webserver.keep_alive()
bot.run("DISCORD_TOKEN")