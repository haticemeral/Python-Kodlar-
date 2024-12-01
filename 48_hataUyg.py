liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

#1- liste elemanlnarı içindeki syısal değerleri bulun
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

#2- kullanıcı 'q' değerini girmedikçe aldığınız her inoutun sayısal değer olup olmadığından emin olunuz aksi halde hata messajı yazın
while True:
    sayi= input('sayi: ')
    if sayi == 'q':
        break
    try:
        result = float(sayi)
        print('girdiğiniz sayı: ', result)
        break
    except ValueError:
        print('geçersiz sayı')
        continue


#3- girilen parola içinde türkçe karakter hatası veriniz
parola = input('parola: ')

def checkPassword(parola):
        
    turkce_karakter = 'şçğüöıİ'
    for i in parola:
        if i in turkce_karakter:
            raise TypeError('parola türkçe karakter içeremez')
        else:
            pass

    print('geçerli parola')

try:
    checkPassword(parola)
except TypeError as err:
    print(err)

#4- faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verin
def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError('negatif değer')
    result = 1
    for i in range(1, x+1):
        result*i
    
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)