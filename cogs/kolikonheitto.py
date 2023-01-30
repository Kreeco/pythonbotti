# -*- coding: cp1252 -*-
from discord.ext import commands
import random


class Kolikonheitto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def kolikko(self, ctx): #ctx = context, komennossa on aina oltava väh. 1 parametri.
        noppa = random.randint(0, 1)
        if noppa == 0:
            await ctx.send('Kruuna.')
        elif noppa == 1:
            await ctx.send('Klaava.')


async def setup(bot):
    await bot.add_cog(Kolikonheitto(bot))