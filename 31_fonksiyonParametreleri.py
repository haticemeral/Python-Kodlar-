def changeName(n):
    n = 'ada'

name = 'yiğit'
changeName(name)
print(name) #fonksiyon önceden tanımlanmış name değişkenini değiştiremez
#ekran çıktısı=>yiğit


def change(n):
    n[0] = 'istanbul' #adres kopyalandı ve kullanıldı

sehirler = ['ankara', 'izmir']
change(sehirler)
print(sehirler) #fonksiyon önceden tanımlanmış liste tipindeki değişken ile kullanıldığından değişken değişir
#ekran çıktısı=>['istanbul', 'izmir']


sehirler = [ 'ankara', 'izmir']
n = sehirler[:] #slicing (: tüm bilgileri alır. 0:2 de yazabilridik)
#tüm diziyi n değişkeninin içine atayıp kopyaladık
n[0] = 'istanbul'
print(sehirler) #['ankara', 'izmir']
print(n) #['istanbul', 'izmir']

def add(a,b,c=0):
    return sum((a,b,c)) #sum python ile gelen hazır bir fonksiyondur toplama işlemi yapar
#2 parametre gönderildiğinde de 3 parametre gönderildiğinde de çalışır
print(add(10,30))

def topla(*params):
    print(params) #gönderilen tüm parametreleri liste şeklinde yazdırır
    print(params[3]) #gönderilen parametrelerden [3] indisli elemanı yazdırır
    return sum(params) #kaç parametre gönderilirse gönderilsin çalışır


#sum fonksiyonu kullanmadan fonksiyon yazalım
def toplam(*params): #değişken sayıda parametre kullanacağımızı ve tuple(liste) olduğunu belli etmek için * kullandık
    sum = 0
    for n in params:
        sum += n
    return sum

print(toplam(29,58,50,23,55,3))

def displayUser(**args): #dictinary olduğunu belli etmek için ** kullandık
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayUser(name = 'çınar', age = 2, city = 'istanbul')
displayUser(name = 'ada', age = 12, city = 'kocaeli', phone = '123244')
displayUser(name = 'yiğit', age = 14, city = 'ankara', phone = '123441', email = 'yigit@hgmail.com')


def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = 'value 2')
"""ekran çıktısı
10
20
(30, 40, 50)
{'key1': 'value 1', 'key2': 'value 2'}
"""