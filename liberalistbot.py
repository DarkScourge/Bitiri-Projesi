import os
import discord
from discord.ext import commands
import random
import requests
import certifi
import time
import asyncio

tanım = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='L', tanım=tanım, intents=intents)



komutlar = ["/yardım: Kullanılabilir komutları gösterir.", "/yazı_tura: Bota yazı tura attırır","Bota istenilen sayıda istenilen mesajlar attırılır (Sadece moderatörler)", ]

# Soru Cevap Sözlüğü
soru_ve_cevap = {
    'sa': 'as',
    'selamunaleyküm': 'Vealeykümselam ve rahmetullahi ve berekatu.',
    'selamaleküm': 'Vealeykümselam ve rahmetullahi ve berekatu.',
    'merhaba': 'Selam',
    'selam': '🫡',
    'naber': 'Züper',
    'naber kanki': 'Züper',
    'naber lan': 'züper',
    'naber la': 'züper',
    'napıyon': 'Dolabında oturuyorum',
    'nabıyon': 'Dolabında oturuyorum', 
    'napıyon lan': 'İyidir kankim sen napıyon',
    'nasılsın': 'Hayat çok zor',
    'pşt': 'Hoşt',
    'ben de iyiyim': 'Sordum mu la',
    'hep iyi ol': 'Sulanıyon mu lan sen bana',
    'hep züper ol': 'Sende bebiş',
    'sensin bebiş': 'Eywallah',
    'neden': 'Kaplumbağa deden xD',
    'ye beni': 'Hammm',
    'liberalist': 'Buyur',
    'sus': 'üzdün :((',
    'eşşek': 'At',
    'eşek': 'At',
    'salak': 'ŞAPŞİK 🤡',
    'sen kimsin': 'Çağlar öncesi zamanlardan kalma bir varlık, şahsiyet veya bir canlı. Ve sen de bana itaat etmek için gönderilen zavallı bir kulsun.',
    'bs vs gel': 'Daha dün babanı yendim ağlıyo şu an',
    'ne diyon la': 'Diyom ki OSSURDUM',
    'küsme': 'Tamam hadi hadi küsmedim',
    'küsme la': 'Tamam hadi hadi küsmedim',
    'annen var mı': 'Askerde',
    'baban var mı': 'Mutfakta',
    'benle sevgili ol': 'Dünden hazırım aşkımmm 😍',
    'ayp': 'Bencede',
    'ayb': 'Bencede',
    'bencede': 'Sana fikrini soran olmadı la.',
    'yavrum': 'ŞAPŞİK',
    'aşkım': 'MUCKKK',
    'bb': 'Öpüyorum bal dudaklarından',
    'ez': 'EZ çerEz mayonEZ patatEZ fotosentEZ sentEZ  merkEZ bEZ gEZ tEZ obEZ diyEZ eğrEZ falEZ güvEZ kepEZ melEZ ortEZ pünEZ ançüEZ körfEZ menfEZ müfrEZ pekmEZ antitEZ çekelEZ hipotEZ protEZ trapEZ trampEZ çerkenEZ çömEZ prEZ görünmezEZ erEZ sevmEZ kesmEZ istemEZ terlemEZ sevilmEZ sevdirilmEZ görülmEZ süzülmEZ sövülmEZ çözülmEZ serpilmEZ biçilmEZ erilmEZ ölmEZ yenilmEZ serilmEZ evrilmEZ çevrilmEZ erimEZ övülmEZ muvaffakiyetsizleştirilmEZ buvatanbölünmEZ.',
    'bu kadar kaba olma': 'Özür dilerim 😭',
    'çok kabasın': 'Özür dilerim 😭',
    'üzdün beni': 'Özür dilerim 😭',
    'ayıp ettin': 'Özür dilerim 😭',
    'seni seviyorum': 'Tezgah lan bu',
    'ağlama o zaman': 'Kırıldım :(('
}



randombilgicevap = [
        'Kirlettiğimiz ozon tabakası 5-10 km arası bir kalınlıktadır.',
        'Mavi geri dönüşüm kutusunun içerisine kaüıt, cam, metal ve plastikler atılmalıdır.',
        'Yeşil geri döüşüm kutusunun içerisine organik atıklar atılabilir.',
        'Sarı geri dönüşüm kutusunun içersinie dönüştürülemeyen ev atıkları atılmalıdır.',
        "Dünya'nın ortalama 1,75 milyar yıllık bir ömrü kaldı."
        "Pisa Kulesi'nin üzerine kurulu olduğu, daha inşaat bitmeden eğilmeye başlamasına sebep olan yumuşak toprak, kulenin 4 farklı depremden sağlam çıkmasını sağlamıştır."
        "Hesaplamalara göre dünyanın  %1.7’si sarhoştur."
        "Sümüklü böcekler fare zehri yemekten hoşlanırlar. Fare zehri onlara şeker gibi gelir ve zehirlenmelerine neden olmaz."
        "İneklerin her sene öldürdüğü insan sayısı, köpek balıklarının öldürdüğü insan sayısından fazladır."
        "Su samurları uyurken el ele tutuşurlar."
        "İkinci Dünya Savaşı'nda zarar gören uçakların sayısı, bugün dünya üzerindeki uçakların sayısından daha fazlaydı."
        "Bebeklerin dört yaşına gelene kadar diz kapakları oluşmaz."
        "Fırsat olduğunda kelebeklerin, kanınızı seve seve içeceklerini biliyor muydunuz?"
        "Norveç ve Kuzey Kore arasında sadece tek bir ülke vardır."
        "Rusya, Plüton'dan daha büyüktür."
]

# BlackJack Altyapısı

# Kart Değerleri
kart_değerleri = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Kart Destesi Oluşturma
def deste_olusturma():
    deste = []
    for takım in ['Kupa', 'Karo', 'Sinek', 'Maça']:
        for sayı in kart_değerleri.keys():
            deste.append((sayı, takım))
    random.shuffle(deste)
    return deste

# El Puanını Hesaplama
def eldeki_degeri_hesaplama(el):
    deger = 0
    aslar = 0
    for kart, suit in el:
        deger += kart_değerleri[kart]
        if kart == 'A':
            aslar += 1
    while deger > 21 and aslar:
        deger -= 10
        aslar -= 1
    return deger

# Kartları Formatlama
def eli_sifirlama(el):
    return ', '.join([f'{kart} {suit}' for kart, suit in el])

# Oyun Kilidi
aktif_oyun = set()



# Yardım
@bot.hybrid_group()
async def l1(ctx):
    await ctx.send()

@l1.command(description="Kullanılabilir komutları gösterir")
async def yardım(ctx):
    await ctx.send(komutlar, ephemeral=True)


# Yazı Tura
@bot.hybrid_group()
async def l2(ctx):
    await ctx.send()


@l2.command(description="Bota yazı tura attırır")
async def yazı_tura(ctx):
    sonuc = random.choice(['yazı', 'tura'])
    await ctx.send('Yazı tura atıyorum')
    time.sleep(1)
    await ctx.send('Veee...')
    time.sleep(2)
    await ctx.send(f'Sonuç: {sonuc}')
    time.sleep(3)



# Tekrarlama
@bot.hybrid_group()
async def l3(ctx):
    await ctx.send()

@l3.command(description="Botun istenilen sayıda istenilen mesajlar atılmasını sağlar (Sadece moderatörler)")
async def tekrarla(ctx, yazi: str, tekrar: int): 
    """Repeats a message multiple times."""
    if ctx.author.id == 194916320997801984:
        for i in range(tekrar):
            await ctx.send(yazi)
            time.sleep(1)
    else:
        await ctx.send('PUHAHAHA. Zibidy sana yetki vermemiş gibi duruyor')



# Random Mem Gönderme
@bot.hybrid_group()
async def l4(ctx):
    await ctx.send()

@l4.command(description="Botun rastgele bir mem göndermesini sağlar")
async def randommem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(3)


# Random Ördek Gönderme
@bot.hybrid_group()
async def l5(ctx):
    await ctx.send()

@l5.command(description="Botun random bir ördek fotoğrafı göndermesini sağlar")
async def randomduck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    time.sleep(3)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


# Random Köpek Gönderme
@bot.hybrid_group()
async def l6(ctx):
    await ctx.send()

@l6.command(description="Botun random bir köpek fotoğrafo göndermesini sağlar")
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    time.sleep(3)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


# Random Bİlgi
@bot.hybrid_group()
async def l7(ctx):
    await ctx.send()

@l7.command(description="Botun random bir bilgi vermesini sağlar")
async def randombilgi(ctx):
    cevap = random.choice(randombilgicevap)
    await ctx.send(cevap)
    time.sleep(3)


# Mesaj Silme
@bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, sayi: int):
    if sayi < 1 or sayi > 100:
        await ctx.send('Silinecek mesaj sayısı 1 ile 100 arasında olmalıdır.')
        return
    
    await ctx.channel.purge(limit=sayi)
    await ctx.send(f'{sayi} mesajlar silindi.', delete_after=5)



# Soru Cevap
@bot.command("s")
async def soru_cevap_cıktı(ctx, *, soru: str):
    cevap = soru_ve_cevap.get(soru, 'Ne diyon la')
    await ctx.send(cevap)
    time.sleep(3)


# BlackJack
@bot.command("bj")
async def blackjack(ctx):
    if ctx.author.id in aktif_oyun:
        await ctx.send('Zaten bir oyununuz var! Lütfen oyununuzu bitirin.')
        return

    aktif_oyun.add(ctx.author.id)

    try:
        deste = deste_olusturma()
        oyuncunun_eli = [deste.pop(), deste.pop()]
        dealerin_eli = [deste.pop(), deste.pop()]

        oyuncunun_puanı = eldeki_degeri_hesaplama(oyuncunun_eli)
        dealerin_puanı = eldeki_degeri_hesaplama(dealerin_eli)

        await ctx.send(f'Eliniz: {eli_sifirlama(oyuncunun_eli)} (Puan: {oyuncunun_puanı})')
        await ctx.send(f'Dealer\'ın görünen kartı: {dealerin_eli[0][0]} {dealerin_eli[0][1]}')

        while oyuncunun_puanı < 21:
            await ctx.send('Hit veya Stand? (h/s)')
            try:
                msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30.0)
            except asyncio.TimeoutError:
                await ctx.send('Zaman doldu! Oyun sona erdi.')
                return

            if msg.content.lower() == 'h':
                oyuncunun_eli.append(deste.pop())
                oyuncunun_puanı = eldeki_degeri_hesaplama(oyuncunun_eli)
                await ctx.send(f'Eliniz: {eli_sifirlama(oyuncunun_eli)} (Puan: {oyuncunun_puanı})')
            elif msg.content.lower() == 's':
                break

        if oyuncunun_puanı > 21:
            await ctx.send('Ops! Kaybettiniz.')
            return

        await ctx.send(f'Dealer\'ın eli: {eli_sifirlama(dealerin_eli)} (Puan: {dealerin_puanı})')
        while dealerin_puanı < 17:
            dealerin_eli.append(deste.pop())
            dealerin_puanı = eldeki_degeri_hesaplama(dealerin_eli)
            await ctx.send(f'Dealer\'ın eli: {eli_sifirlama(dealerin_eli)} (Puan: {dealerin_puanı})')

        if dealerin_puanı > 21 or dealerin_puanı < oyuncunun_puanı:
            await ctx.send('Kazandınız!')
        elif dealerin_puanı == oyuncunun_puanı:
            await ctx.send('Berabere!')
        else:
            await ctx.send('Kaybettiniz!')

    finally:
        aktif_oyun.remove(ctx.author.id)



# Kapatma
@bot.command('kapansusamkapan')
async def kapatmak(ctx):
    if ctx.author.id == 194916320997801984:
        await ctx.send("Tamam la gidiyom :((")
        await bot.close()
    else:
        await ctx.send("PUHAHAHA. Zibidy sana yetki vermemiş gibi duruyor")



@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} Çalışmaya Başladı!')
    activity = discord.Game("Aşk kumardan ibarettir dostum")
    await bot.change_presence(status=discord.Status.idle, activity=activity)





bot.run('TOKEN')
