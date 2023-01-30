# -*- coding: cp1252 -*-
from discord.ext import commands
import random


class Numeroarvaus(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def numeroarvaus(self, ctx):
        numero = random.randint(1, 10)
        await ctx.send('Arvaa numero 1-10')

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        msg = await self.bot.wait_for("message", check=check)
        print(msg)
        #print(testimuuttuja)
        if int(msg.content) == numero:
            await ctx.send("Oho, oikein meni! Hyvä!")
        else:
            await ctx.send(f"Hävisit pelin, oikea numero oli {numero}")

async def setup(bot):
    await bot.add_cog(Numeroarvaus(bot))