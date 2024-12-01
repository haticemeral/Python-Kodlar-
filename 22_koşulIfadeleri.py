#İF ELSE YAPISI
username = 'sadıkturan'
password = '1234'

if(username == 'sadıkturan'):
    if(password == '1234'):
        print('hoş geldiniz')
    else:
        print('parola yanlış')
else:
    print('username yanlış')


#İF ELİF YAPISI
x = int(input('x: '))
y = int(input('y: '))

if x > y: 
    print('x y den büyüktür')
elif x == y:
    print('x y ye eşittir')
else:
    print('x y den küçüktür')


num = int(input('sayı: '))

if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')

#UYGULAMALAR
#1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz
#ehliyet alma koşulu en az 18 ve eğitim durumu ya da üniversite olmalıdır
isim = input('isminiz:')
yas = int(input('yaşınız: '))
egitim = input('eğitim: ')
if (yas>=18):
    if (egitim=='lise' or egitim=='üniversite' ):
        print(f'{isim} ehliyet alabilirsiniz')
    else:
        print(f'{isim} ehliyet alamazsınız eğitim durumunuz yetersiz')
else:
    print('ehliyet alamazsınız yaşınız tutmuyor')


#2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre  not aralığına karşılık gelen not bilgisini yazdırınız
# 0-24 =>0
# 25-44 =>1
# 45-54 =>2
# 55-69 =>3
# 70-84 =>4
# 85-100 =>5
yazili1 = float(input('1. yazılı: '))
yazili2 = float(input('2. yazılı: '))
sozlu = float(input('sözlü notu: '))

ortalama = (yazili1 + yazili2 + sozlu)/3

if(ortalama>=0) and (ortalama<25):
    print(f'ortalamanız:{ortalama} notunuz:0')
elif(ortalama>=25) and (ortalama<45):
    print(f'ortalamanız:{ortalama} notunuz:1')
if(ortalama>=45) and (ortalama<55):
    print(f'ortalamanız:{ortalama} notunuz:2')
if(ortalama>=55) and (ortalama<70):
    print(f'ortalamanız:{ortalama} notunuz:3')
if(ortalama>=70) and (ortalama<85):
    print(f'ortalamanız:{ortalama} notunuz:4')
if(ortalama>=85) and (ortalama<100):
    print(f'ortalamanız:{ortalama} notunuz:5')
else:
    print('yanlış bilgi girdiniz')