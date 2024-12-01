x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6
 
#1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir
a = int(input("1.sayı: "))
b = int(input("2.sayı: "))
sonuc = a*b-(x+y+z)
print(sonuc) 

#2- y'nin x'e kalansız bölümünü hesaplayınız
y //= x

#3-(x,y,z) toplamının mod 3'ü nedir
print((x+y+z)%3)

#4- y'nin x. kuvvetini hesaplayınız
print(y ** x)

#5- x, *y, z = numbers işlemşne göre z nin küpü kaçtır
x, *y, z = numbers #(1, [5, 7, 10], 6) yani z = 6 olur
print(z ** 3)

#6- x, *y, z = numbers işlemşne göre y nin değerleri toplamı kaçtırkaçtır
x, *y, z = numbers #(1, [5, 7, 10], 6) yani y değerleri toplamı 22 olur
sonuc = y[0] + y[1] + y[2]
print(sonuc)