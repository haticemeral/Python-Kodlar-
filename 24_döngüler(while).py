# 1den 100e kadar yazma
x = 1
while x<=100:
    print(x)
    x+=1

# 1den 100e kadar çift olan sayıları yazma
x = 1
while x<=100:
    if(x%2==0):
       print(x)
    x += 1 

name = '' #false değerdir
while not name: #değer true döndüğünde
    name = input('isminizi giriniz: ')
print(f'merhaba, {name}')


#UYGULAMALAR

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
#1- sayilar listesini while ile ekrana yazdırınız
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

#2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek syıları ekrana yazdırın
baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))
i = baslangic
while i < bitis:
    i += 1
    if(i%2==1):
        print(i)

#3- 1-100 arasındaki sayıları azalan şekilde yazdırın
x = 100
while x>0:
    print(x)
    x-=1

#4- kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
numbers = [] #içi boş bir liste
i = 0
while i<5:
    sayi = int(input('sayı: '))
    numbers.append(sayi)
    i+=1
    numbers.sort() #sıralama fonksiyonu
print(numbers)

#5- kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız
#   ürün sayısını kullanıcıya sorun
#   dictionary listesi yapın (name,price) şeklinde olsun
#   ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin
urunler = []
adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i = 0
while (adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i+=1

for urun in urunler:
    print(f'ürün ad: {urun["name"]} ürün fiyatı: {urun["price"]}')