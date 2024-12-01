numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

for a in numbers:
    print(a)

for a in numbers:
    print('hello')  # 5 kez hello yazar

names = ['çınar', 'sadık', 'sena']
for name in names:
    print(f'my name is {name}')

name = 'sadık turan'
for n in name:
    print(n) #her karakteri teker teker yazdırır


tuple = (1, 2, 3, 4, 5)
for t in tuple:
    print(t) #tüm elemanları teket teker yazdırır

tuple = [(1,2), (1,3), (3,5), (5,7)]
for t in tuple:
    print(t) #sıralı ikilileri ( , ) şeklinde yazdırır

for a,b in tuple:
    print(a) # (a,b) şeklindeki sıralı ikililerin sadece a değerini yazdırır

for a,b in tuple:
    print(a,b) #(a,b) şeklindeki sıralı ikilileri a b şeklinde yazdırır

d = {'k1':1, 'k2':2, 'k3':3} #dictinary
for item in d:
    print(item) # sadece key bilgilerini yazdırır=>k1 k2 k3 gibi

for item in d.items:
    print(item) #eleman gruplarına ulaşır=>('k1', 1) gibi

for key, value in d.items:
    print(key) #anahtarları yazdırır=>k1 gibi

for key, value in d.items:
    print(key, value) #hem key hem anahtarı yan yana yazdırır=> k1 1 gibi

#UYGULAMALAR
sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

#1- sayilar listesindeki hangi sayılar 3 ün katıdır
for sayi in sayilar:
    if(sayi%3==0):
        print(sayi)


#2- sayilar listesindeki sayıların toplamı kaçtır
toplam = 0
for sayi in sayilar:
    toplam += sayi

#3- sayılar listesindeki tek sayılların karesini alınız
for sayi in sayilar:
    if(sayi%2==1):
        print(sayi**2)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

#4- şehirlerin hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)



urunler = [ 
    {'name':'samsung s6', 'price':'3000'},
    {'name':'samsung s7', 'price':'4000'},
    {'name':'samsung s8', 'price':'5000'},
    {'name':'samsung s9', 'price':'6000'},
    {'name':'samsung s10', 'price':'7000'}
]
#5- ürünlerin fiyatları toplamı kaçtır
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)
#6- ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])