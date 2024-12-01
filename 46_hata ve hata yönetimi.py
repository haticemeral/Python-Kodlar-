#error=> hata
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) =>ZeroDivisionError
# print('denem'e) => SyntaxError


#error handling => hata yönetimi
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print("yanlış bilgi girdiniz")
    print(e) #hatanın sebebini de yazdırır

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print("yanlış bilgi girdiniz")
else:
    print('her şey yolunda') #hata bulunmaması durumunda yazdırır

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except (ZeroDivisionError, ValueError) as e:
        print("yanlış bilgi girdiniz")
    else:
        break #bilgiler doğru girildiğinde döngüden çıkar

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex: #hataları kontrol eder
        print("yanlış bilgi girdiniz", ex)
    else:
        break


while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex: #hataları kontrol eder
        print("yanlış bilgi girdiniz", ex)
    else:
        break
    finally:
        print('try exept sonlandı')