# -*- coding: cp1252 -*-
import os
import sys
import discord #kirjasto discord-botin määrittämiseen
from discord.ext import commands #Discord-komentojen kirjasto
import asyncio
import hashlib
import random
from cogs.cogiskriptit.sd_generoija import kuva #kuvanpostausfunktiomoduuli
from scripts.kuvauta import SDBot
#haetaan  Stable Diffusionin SDBot-komento joka on muokattu botin ajettavaksi kuvagenerointifunktioksi.


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = commands.when_mentioned_or("!"),
            # command_prefixillä määritellään millä erikoismerkillä botti ottaa käskyjä vastaan käyttäjältä
            intents = discord.Intents.all())
            #discordissa pitää nykyään antaa "luvat" intentseillä jotta botti voi vastaanottaa käskyjä

    async def setup_hook(self): #ladataan cogsit eli luokka-moduulit joihin toiminnot on jaettu
        print(f"\033[31mKirjaudutaan sisään käyttäjänä {bot.user}\033[39m")
        cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}/cogs"
        for filename in os.listdir(cogs_folder): #haetaan kaikki cogsit kansiosta
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                #tässä poistetaan nimen päädystä 3 viimeistä merkkiä eli ".py" päätteen
        await bot.tree.sync()
        print("Rattaat viritetty.") #printataan viesti konsoliin, että cogit on ladattu onnistuneesti


queues = []
blocking = False
sd_bot = SDBot()
loop = None
bot = Bot()


k = open("J:\Python\Botti_token.txt", "r")
#avataan botin API-key erillisestä tekstitiedostosta.
token = k.read()
k.close()


async def main():
    async with bot:
        await bot.start(token)
#tällä komennolla botti "käynnistyy" eli koodi ottaa yhteyden discordin bottikäyttäjään, token käyttäjän avaimen.


@bot.event
async def on_ready():
	print('Signaali vastaanotettu Discord-asemasta, yksikkö {0.user} on valmiustilassa.'.format(bot))



@bot.command(case_insensitive = True, aliases = ["generoi","generate", "kuvauta"])
async def makeimg(ctx, prompt):
    global loop
    loop = asyncio.get_running_loop()
    print(loop)
    que(ctx, prompt)
    await ctx.send(f'Generoidaan kuvapyyntöä "{prompt}", mylly käynnistyy. :gear:')

    if blocking:
        print('blokkaa')
        await ctx.send("Kuvangenerointi on kesken. :x:")
    else:
        await asyncio.get_running_loop().run_in_executor(None, sd_gen, ctx, queues)
        await kuva(ctx)



def sd_gen(ctx, queues):
    global blocking
    print(queues)
    if len(queues) > 0:
        blocking = True
        prompt = queues.pop(0)
        prompt = list(prompt.values())[0]
        filename = hashlib.sha256(prompt.encode('utf-8')).hexdigest()[:20]
        if 'seed' in prompt.lower():
            try:
                seed = int(prompt.split('seed')[1].split('=')[1].strip())
            except:
                seed = random.randint(0, 4294967295)
            prompt = prompt.split('seed')[0]
        else:
            seed = random.randint(0, 4294967295)

        sd_bot.makeimg(prompt, filename, seed)
        sd_gen(ctx, queues)
    else:
        blocking = False


def que(ctx, prompt):
    user_id = ctx.message.author.mention
    queues.append({user_id: prompt})
    print(f'"{prompt}" lisätty jonoon. ')


def check_num_in_que(ctx):
    user = ctx.message.author.mention
    user_list_in_que = [list(i.keys())[0] for i in queues]
    return user_list_in_que.count(user)




asyncio.run(main())
