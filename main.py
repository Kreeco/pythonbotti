# -*- coding: cp1252 -*-

import discord
import random
from discord.ext import commands #kirjasto, jonka avulla botti voi vastaanottaa discord-komentoja. Nyky��n my�s "slash"-komennot mahdollisia, jotka toimivat eri tavalla.

intents = discord.Intents.default() #disccordissa pit�� nyky��n antaa "luvat" intentseill� jotta botti voi vastaanottaa k�skyj�
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents) #command_prefixill� m��ritell��n mill� erikoismerkill� botti ottaa k�skyj� vastaan k�ytt�j�lt�


@bot.command(name='test1', aliases=['t1']) #testi jolla n�kee ottaako botti k�skyj� vastaan
async def test1(ctx):
    print('test command')

@bot.command()
async def kolikko(ctx): #ctx = context, komennossa on aina oltava v�h. 1 parametri.
    noppa = random.randint(0, 1)
    print(noppa)
    if noppa == 0:
        await ctx.send('Kruuna.')
    elif noppa == 1:
        await ctx.send('Klaava.')


@bot.command()
async def blackjack(ctx):
    maat = (":hearts:", ":diamonds:", ":spades:", ":clubs:") #kaksoispisteet sanan ymp�rill� printtaavat suoraan emojin discordiin
    rankit = ("Kaksi", "Kolme", "Nelj�", "Viisi", "Kuusi", "Seitsem�n", "Kahdeksan", "Yhdeks�n", "Kymmenen", "J�tk�", "Kuningatar", "Kuningas", "�ss�")
    arvot = {"Kaksi":2,"Kolme":3, "Nelj�":4, "Viisi":5, "Kuusi":6, "Seitsem�n":7, "Kahdeksan":8, "Yhdeks�n":9, "Kymmenen":10, "J�tk�":10, "Kuningatar":10, "Kuningas":10, "�ss�":11}

    pelaa = True

    class Kortti:
        def __init__(self,maa,rankki):
            self.maa = maa
            self.rankki = rankki

        def __str__(self):
            return self.rankki + self.maa

    class Pakka:
        def __init__(self):
            self.pakka = [] #aloitetaan tyhj�ll� pakalla
            for maa in maat:
                for rankki in rankit:
                    self.pakka.append(Kortti(maa,rankki)) #rakennetaan kortit ja lis�t��n ne listaan

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

    class K�si:
        def __init__(self):
            self.kortit = [] #alussa k�si on tyhj�
            self.arvo = 0 #alussa k�den arvo on 0
            self.�ss�t = 0 #t�ll� seurataan �ssi�

        def lis��_kortti(self,kortti):
            self.kortit.append(kortti)
            self.arvo += arvot[kortti.rankki]
            if kortti.rankki == "�ss�":
                self.�ss�t += 1

        def �ss�_s��t�(self): #�ss� voi olla blackjackissa 11 tai 1, t�ss� voidaan s��t�� arvo tilanteen mukaan.
            while self.arvo > 21 and self.�ss�t:
                self.arvo -= 10
                self.�ss�t -= 1

    testaa_pakka = Pakka()
    testaa_pakka.sekoita()
    testaa_pelaaja = K�si()
    testaa_pelaaja.lis��_kortti(testaa_pakka.diilaa())
    testaa_pelaaja.lis��_kortti(testaa_pakka.diilaa())
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

        def h�vi�_betti(self):
            self.saldo -= self.bet

    def ota_panos(pelimerkit):
       while True:
            try:
                pelimerkit.bet = pelaajabetti
            except ValueError:
                #await ctx.send("T�ytyy olla numero!")
                pass
            else:
                if pelimerkit.bet > pelimerkit.saldo:
                    #await ctx.send("Sinulla on liian v�h�n pelimerkkej�",pelimerkit.saldo)
                    pass
                else:
                    break
    def ly�nti(pakka,k�si):
        k�si.lis��_kortti(pakka.diilaa())
        k�si.�ss�_s��t�()

#    def ly�nti_vai_j��(pakka,k�si):
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
        await ctx.send("Oho, oikein meni! Hyv�!")
    else:
        await ctx.send(f"H�visit pelin, oikea numero oli {numero}")




@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

k = open("J:\Python\Botti_token.txt", "r") #avataan botin API-key erillisest� tekstitiedostosta.
token = k.read()
k.close()

bot.run(token) #t�ll� komennolla botti "k�ynnistyy" eli koodi ottaa yhteyden discordin bottik�ytt�j��n, token k�ytt�j�n avaimen.

