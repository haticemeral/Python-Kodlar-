def greeting(name):
    print("hello"+name)


#!fonksiyonun normal kullanımı
# greeting("ali")
# print(greeting)

#!fonkdiyonun başka değişkene atılıp kullanımı(adres bilgisiyle beraber atandığı için ikisi de aynı işi yapar)
sayHello =  greeting
print(sayHello("ali"))
print(greeting("ali"))

# #del sayHello #sayHello yu silsek bile greeting i hala kullanabiliriz
# print(sayHello)
# print(greeting)


#? ENCAPSULATİON (İÇ İÇE FONKSİYONLAR)
def outer(num1):
    print('outer') #dış fonksiyonda olduğumuzu görmek için
    def inner_increment(num1):
        print('inner')  #iç fonksiyonda olduğumuzu görmek için
        return num1 + 1
    num2 = inner_increment(num1)#içerideki fonksiyonun çalışması için dışardaki fonksiyon içinde çağrılmış olması gerekir
    print(num1, num2)

outer(10) #fonksiyonu parametre ile çağırdık
#inner_increment(10)#hata alırız çünkü sadece outer kapsamında çalıştırılabilir


def factorial(number):
    if not isinstance(number, int): #isinstance fonksiyonu gönderilen ilk parametrenin, ikici parametre türünden olup olmadığını kontrol eder
        raise TypeError("number must be an integer")
    if not number >=0:
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if number<=1:
            return 1
        
        return number * inner_factorial(number - 1)
    
    return inner_factorial(number)

try:
    print(factorial('4'))
except Exception as ex:
    print(ex)

print(factorial(5))