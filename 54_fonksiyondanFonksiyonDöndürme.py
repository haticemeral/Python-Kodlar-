# RETURNİNG
#örnek1
def usalma(number):
    #two = usalma(2)
    #three = uslama(3)

    def inner(power):
        return number ** power
    
    return inner #fonskiyonu geri döndürdük

two = usalma(2)
three = usalma(3)
print(two(3)) #8
print(three(4)) #81


#örnek2
def yetki_sorgula(page):
    def inner(role):
        if role == 'admin':
            return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
    return inner


user1 = yetki_sorgula("product edir")
print(user1("admin"))
print(user1("user"))



#örnek3
def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma
    

toplama = islem("toplama")
print(toplama(1,2,3,4,5,6,7))

carpma = islem("carpma")
print(carpma(1,2,4,6,7))


#****FONKSİYONA BAŞKA BİR FONKSİYONU PARAMETRE OLARAK GÖNDERME
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(3,4))
    elif islem_adi == "bolme":
        print(f4(10,2))
    else:
        print("gecersiz islem")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "kökalma")


#******DECORATOR FONKSİYONLAR=>kod tekrarının önüne geçer
#belli bir fonksiyona başka özellikler eklemek için kullanılır
def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator #decorator söz dizimi bu şekildedir
def  sayHello(name): #decorator fonksiyonunun parametresi olan func fonksiyonu bu fonksiyon olmuş olur
    print("hello",name)

def sayGreeting():
    print("greeting")

# sayHello = my_decorator(sayHello) #tetikledik(söz dizimini kullanmadan yapılabilir)
# sayHello()

sayHello("ali")

#örnek2


import math
import time #işlem süresini ölçmek için kullandık

def usalma(a,b):
    start = time.time()
    time.sleep(1) #geçerli iş parçacığının yürütülmesini 1 saniye durdurur

    print(math.pow(a,b))

    finish = time.time()
    print("fonksiyon " + str(finish-start) + " saniye sürdü")

def faktoriyel(num):
    start = time.time()
    time.sleep(1)

    print(math.factorial(num))

    finish = time.time()
    print("fonksiyon " + str(finish-start) + " saniye sürdü")


usalma(2,3)

faktoriyel(4)


#bu iki fonksiyon sadece kendi işini yapsın ve süreyi başka bir fonksiyon ortak olarak hesaplasın
import math
import time #işlem süresini ölçmek için kullandık

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__ + " " + str(finish-start) + " saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)