# -*- coding: cp1252 -*-

import discord
import random
from discord.ext import commands #kirjasto, jonka avulla botti voi vastaanottaa discord-komentoja. Nykyään myös "slash"-komennot mahdollisia, jotka toimivat eri tavalla.

intents = discord.Intents.default() #disccordissa pitää nykyään antaa "luvat" intentseillä jotta botti voi vastaanottaa käskyjä
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents) #command_prefixillä määritellään millä erikoismerkillä botti ottaa käskyjä vastaan käyttäjältä


@bot.command(name='test1', aliases=['t1']) #testi jolla näkee ottaako botti käskyjä vastaan
async def test1(ctx):
    print('test command')

@bot.command()
async def kolikko(ctx): #ctx = context, komennossa on aina oltava väh. 1 parametri.
    noppa = random.randint(0, 1)
    print(noppa)
    if noppa == 0:
        await ctx.send('Kruuna.')
    elif noppa == 1:
        await ctx.send('Klaava.')


@bot.command()
async def blackjack(ctx):
    maat = (":hearts:", ":diamonds:", ":spades:", ":clubs:") #kaksoispisteet sanan ympärillä printtaavat suoraan emojin discordiin
    rankit = ("Kaksi", "Kolme", "Neljä", "Viisi", "Kuusi", "Seitsemän", "Kahdeksan", "Yhdeksän", "Kymmenen", "Jätkä", "Kuningatar", "Kuningas", "Ässä")
    arvot = {"Kaksi":2,"Kolme":3, "Neljä":4, "Viisi":5, "Kuusi":6, "Seitsemän":7, "Kahdeksan":8, "Yhdeksän":9, "Kymmenen":10, "Jätkä":10, "Kuningatar":10, "Kuningas":10, "Ässä":11}

    pelaa = True

    class Kortti:
        def __init__(self,maa,rankki):
            self.maa = maa
            self.rankki = rankki

        def __str__(self):
            return self.rankki + self.maa

    class Pakka:
        def __init__(self):
            self.pakka = [] #aloitetaan tyhjällä pakalla
            for maa in maat:
                for rankki in rankit:
                    self.pakka.append(Kortti(maa,rankki)) #rakennetaan kortit ja lisätään ne listaan

        def __str__(self):
            koko_pakka = ""
            for kortti in self.pakka:
                koko_pakka += "\n" +kortti.__str__()
            return "Pakassa on " + koko_pakka

        def sekoita(self):
            random.shuffle(self.pakka)

        def diilaa(self):
            yksi_kortti = self.pakka.pop()
            return yksi_kortti

    class Käsi:
        def __init__(self):
            self.kortit = [] #alussa käsi on tyhjä
            self.arvo = 0 #alussa käden arvo on 0
            self.ässät = 0 #tällä seurataan ässiä

        def lisää_kortti(self,kortti):
            self.kortit.append(kortti)
            self.arvo += arvot[kortti.rankki]
            if kortti.rankki == "Ässä":
                self.ässät += 1

        def ässä_säätö(self): #ässä voi olla blackjackissa 11 tai 1, tässä voidaan säätää arvo tilanteen mukaan.
            while self.arvo > 21 and self.ässät:
                self.arvo -= 10
                self.ässät -= 1

    testaa_pakka = Pakka()
    testaa_pakka.sekoita()
    testaa_pelaaja = Käsi()
    testaa_pelaaja.lisää_kortti(testaa_pakka.diilaa())
    testaa_pelaaja.lisää_kortti(testaa_pakka.diilaa())
    testaa_pelaaja.arvo



    def check(testimuuttuja):
        return testimuuttuja.author == ctx.author and testimuuttuja.channel == ctx.channel

    await ctx.send("Anna betti.")
    pelaajabetti = await bot.wait_for("message", check=check)

    for kortti in testaa_pelaaja.kortit:
        await ctx.send(kortti)





    class Pelimerkit():
        def __init__(self):
            self.saldo = 100
            self.bet = 0

        def voita_betti(self):
            self.saldo += self.bet

        def häviä_betti(self):
            self.saldo -= self.bet

    def ota_panos(pelimerkit):
       while True:
            try:
                pelimerkit.bet = pelaajabetti
            except ValueError:
                #await ctx.send("Täytyy olla numero!")
                pass
            else:
                if pelimerkit.bet > pelimerkit.saldo:
                    #await ctx.send("Sinulla on liian vähän pelimerkkejä",pelimerkit.saldo)
                    pass
                else:
                    break
    def lyönti(pakka,käsi):
        käsi.lisää_kortti(pakka.diilaa())
        käsi.ässä_säätö()

#    def lyönti_vai_jää(pakka,käsi):
#       global pelataan

 #       while True:



@bot.command()
async def numeroarvaus(ctx):
    numero = random.randint(1, 10)
    await ctx.send('Arvaa numero 1-10')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await bot.wait_for("message", check=check)
    print(msg)
    #print(testimuuttuja)
    if int(msg.content) == numero:
        await ctx.send("Oho, oikein meni! Hyvä!")
    else:
        await ctx.send(f"Hävisit pelin, oikea numero oli {numero}")




@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

k = open("J:\Python\Botti_token.txt", "r") #avataan botin API-key erillisestä tekstitiedostosta.
token = k.read()
k.close()

bot.run(token) #tällä komennolla botti "käynnistyy" eli koodi ottaa yhteyden discordin bottikäyttäjään, token käyttäjän avaimen.

