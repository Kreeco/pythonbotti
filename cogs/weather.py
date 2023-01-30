# -*- coding: cp1252 -*-
from discord.ext import commands
import requests
import discord


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sää(self, ctx, *, city: str): #sää-komennolla haetaan säätiedot openweathermap-sivustolta käyttäen requests-kirjastoa ja API-avainta
        k = open("J:\Python\Sää_token.txt", "r")  # avataan sään API-key erillisestä tekstitiedostosta.
        weather_token = k.read()
        k.close()
        weather_osoite = "http://api.openweathermap.org/data/2.5/weather?"
        kaupunki_nimi = city
        complete_url = weather_osoite + "appid=" + weather_token + "&q=" + kaupunki_nimi
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsius = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Sää paikassa {kaupunki_nimi}",
                                  color=ctx.guild.me.top_role.color, timestamp=ctx.message.created_at,)
            embed.add_field(name="Sään kuvaus", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Lämpötila(C)", value=f"**{current_temperature_celsius}°C**", inline=False)
            embed.add_field(name="Ilmankosteus(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Ilmanpaine(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Säätiedot pyytänyt käyttäjä {ctx.author.name}")
            await channel.send(embed=embed)
        else:
            await channel.send("Annettua paikkaa ei löytynyt.")

async def setup(bot):
    await bot.add_cog(Weather(bot))