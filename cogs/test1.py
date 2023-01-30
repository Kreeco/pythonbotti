# -*- coding: cp1252 -*-
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test1', aliases=['t1']) #testi jolla näkee ottaako botti käskyjä vastaan
    async def test1(self, ctx):
        print('test command')

async def setup(bot):
    await bot.add_cog(Test(bot))