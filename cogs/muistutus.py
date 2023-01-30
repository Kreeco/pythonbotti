# -*- coding: cp1252 -*-
from discord.ext import commands
import discord
import asyncio
from datetime import datetime, timedelta

class Muistutus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
    #@commands.bot_has_permissions(attach_files = True, embed_links = True)
    async def muistutus(self, ctx, time, *, reminder):
        print(time)
        print(reminder)
        user = ctx.message.author
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
        seconds = 0
        if reminder is None:
            embed.add_field(name='Varoitus', value='Määritä mistä tahdot minun muistuttavan.') # Virheviesti-ilmoitus
        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} päivää"
        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} tuntia"
        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minuuttia"
        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} sekuntia"
        if seconds == 0:
            embed.add_field(name='Varoitus',
                            value='Määritä aika kunnolla. (muodossa s/m/d)')
        elif seconds > 604800:
            embed.add_field(name='Varoitus', value='Liian pitkä aika!\nMaksimiaika on 7 päivää.')
        else:
            await ctx.send(f"Muistutan aiheesta {reminder}  {counter} jälkeen.")
            await asyncio.sleep(seconds)
            await ctx.send(f"Hei {ctx.author.mention}!! Muistutus aiheesta {reminder} jonka asetit {counter} sitten.")
            return
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Muistutus(bot))