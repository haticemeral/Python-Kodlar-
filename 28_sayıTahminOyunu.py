import random
sayi = random.randint(1,10)
hak = 5
sayac = 0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmin: '))
    if sayi==tahmin:
        print(f'tebrikler {sayac}. tahminde bildiniz.')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    if hak==0:
        print(f'hakkınız bitti. tutulan sayı: {sayi}')


