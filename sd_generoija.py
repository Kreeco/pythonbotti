# -*- coding: cp1252 -*-
import os
import discord
import glob


async def kuva(ctx): #etsitään uusin kuva kansiosta
    ts = 0
    found = None
    for file_name in glob.glob('C:\img\*'):
        fts = os.path.getmtime(file_name)
        if fts > ts:
            ts = fts
            found = file_name
    with open(found, 'rb') as f: #otetaan kuvan kopioitu ID ja lähetetään se discordiin
        picture = discord.File(f)
        f.close()
        viesti = f"{ctx.message.author.mention} kuvanne on generoitu, olkaa hyvä. :robot:"
        await ctx.send(file=picture, content=viesti)