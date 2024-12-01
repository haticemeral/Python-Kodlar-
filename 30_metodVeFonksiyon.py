#METODLAR:liste üzerinde önceden tanımlanmış python kütüphanesi ile birlikte gelen liste sınıfının üyesine denir

list = [1, 2, 3]
list.append(4) #listeye 4 elemanını ekleyen metod
list.pop() #listenin som elemanını silen metod
print(type(list)) #tipini gösterir
print(list)

myString = 'hello'
print(myString.upper) #stringteki tüm harfleri büyük yapan metod


#FONKSİYON:metodtan farkı class içinde tanımlanmamış olmasıdır belli amaçlar için oluşturulmuş kod bloklarıdır

def sayHello(): # def anahtar kelimesi fonksiyonun adı :
    print('hello') #fonksiyon çağırıldığında çalışacak kod blopğu

sayHello() #fonksiyonu çağırdık

def sayhello(name): #parametreli fonksiyon
    print('hello ' + name)

sayhello('çınar')

def SayHello(name = 'user'):
    return 'hello' + name

msg = SayHello('ada')
print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10, 29)
print(result)


def yasHesapla(doğumYili):
    return 2023-doğumYili

age = yasHesapla(2003)
print(age)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emekliligeKacYilKaldi>0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('zaten emekli oldunuz')

emekliligeKacYilKaldi(1983, 'ali')