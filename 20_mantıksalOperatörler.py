x = 6
result = 5 < x < 10

#and
result = (x > 5) and (x < 10)
#true, true => true
#true,  false => false 

#or
result = (x > 0) or (x % 2 == 0)
#true, true => true
#true, false => true
#false, false => false

#not
result = not(x > 0)
#not(true) => false
#not(false) => true

print(result)

# UYGULAMALAR
#1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
sayi = float(input('sayi: '))
result = (sayi>0) and (sayi<=100)
print(f"sayı 0-100  arasındadır:{result}")

#2- girilen bir sayının pozitif çift tam sayı olup olmadığını kontrol ediniz
sayi = int(input("sayi: "))
result = (sayi>0) and (sayi % 2==0)
print(f"girilen sayı pozitif çift syı mı {result}")

#3- email ve parola bilgileri ile giriş kontrolü yapınız
email = "emai@sadıkturan"
password = "abc123"
girilenEmail = input("email:")
girilenPassword = input("password: ")
result = (girilenEmail == email) and (girilenPassword == password)
print(f"uygulamaya giriş başarılı mı {result}")

#4-girilen 3 sayıyı büyüklük olarak karşılaştırınız
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
result = (a>b) and (a>c)
print(f"a en büyük sayıdır {result}")
result = (b>a) and (b>c)
print(f"b en büyük sayıdır {result}")
result = (c>a) and (c>b)
print(f"c en büyük sayıdır {result}")

#5- kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
""" formül=(kilo/boy uzunluğunun karesi)
0-18.4 zayıf
18.5-24.9 normal
25.0-29.9 fazla  kilolu
30.0-34.9 şiman(obez)"""
name = input("adınız:")
kg = float(input("kilonuz:"))
hg = int(input("boyunuz:"))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez= (index > 29.9) and (index <= 34.4)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf:{zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal:{normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu:{kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez:{obez}")
