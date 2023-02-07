# -*- coding: cp1252 -*-
import os
import discord
import glob


async def kuva(ctx): #etsit��n uusin kuva kansiosta
    ts = 0
    found = None
    for file_name in glob.glob('C:\img\*'):
        fts = os.path.getmtime(file_name)
        if fts > ts:
            ts = fts
            found = file_name
    with open(found, 'rb') as f: #otetaan kuvan kopioitu ID ja l�hetet��n se discordiin
        picture = discord.File(f)
        f.close()
        viesti = f"{ctx.message.author.mention} kuvanne on generoitu, olkaa hyv�. :robot:"
        await ctx.send(file=picture, content=viesti)