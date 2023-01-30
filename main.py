# -*- coding: cp1252 -*-
import os
import requests
import json
import discord
import random
import asyncio
import time
from datetime import datetime, timedelta
from discord.ext import commands #kirjasto, jonka avulla botti voi vastaanottaa discord-komentoja. Nyky��n my�s "slash"-komennot mahdollisia, jotka toimivat eri tavalla.

#intents = discord.Intents.default() #disccordissa pit�� nyky��n antaa "luvat" intentseill� jotta botti voi vastaanottaa k�skyj�
#intents.message_content = True
#bot = commands.Bot(command_prefix="!", intents=intents) #command_prefixill� m��ritell��n mill� erikoismerkill� botti ottaa k�skyj� vastaan k�ytt�j�lt�

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("!"),
            intents = discord.Intents.all(),
            #help_command = commands.DefaultHelpCommand(dm_help=True)
        )

    async def setup_hook(self): #overwriting a handler
        print(f"\033[31mLogged in as {bot.user}\033[39m")
        cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}/cogs"
        for filename in os.listdir(cogs_folder):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.tree.sync()
        print("Loaded cogs")

bot = Bot()

#async def load_extensions(): #t�ll� saa haettua koko cog-hakemiston kerralla
#    for filename in os.listdir("./cogs"):
#        if filename.endswith(".py"):
#            #poistetaan 3 vikaa eli ".py"
#            await bot.load_extension(f"cogs.{filename[:-3]}")

k = open("J:\Python\Botti_token.txt", "r") #avataan botin API-key erillisest� tekstitiedostosta.
token = k.read()
k.close()


@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


async def main():
    async with bot:
        #await bot.load_extension()
        #await bot.load_extension("cogs.kolikonheitto")
        await bot.start(token)  #t�ll� komennolla botti "k�ynnistyy" eli koodi ottaa yhteyden discordin bottik�ytt�j��n, token k�ytt�j�n avaimen.

asyncio.run(main())
