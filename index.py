import Discord
from discord import Client
from discord.ext import commands
import logging
import discord

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = ''
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_message(message):
    if (message.author == bot.fetch_user("339609439143460867")):
        message.author.send("SHUT THE FUCK UP")
    

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

bot.run(TOKEN)