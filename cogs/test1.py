# -*- coding: cp1252 -*-
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test1', aliases=['t1']) #testi jolla n�kee ottaako botti k�skyj� vastaan
    async def test1(self, ctx):
        print('test command')

async def setup(bot):
    await bot.add_cog(Test(bot))