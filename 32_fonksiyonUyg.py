#1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız 
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('merhaba\n', 10)

#2-kendine gönderilen sınırsız sayıdakş parametreyi bir listeye çeviren fonksiyonu yazınız
def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result = listeyeCevir(20, 30, 40, 'merhaba')
print(result)

#3- gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def asalSayilariBul(syi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi>1:
            for i in range(2, sayi):
                if(sayi % i ==0):
                    break
                else:
                    print(sayi)

sayi1 = int(input('1. sayi: '))
sayi2 = int(input('2. sayi '))
asalSayilariBul(sayi1, sayi2)


#4- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2, sayi):
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))
