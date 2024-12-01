x = input('1. sayi: ') #dışarıdan veri alır
y = input('2. sayi: ')

print(type(x))
print(type(y))

toplam1 = x + y #string birleştime işlemi

toplam2 = int(x) + int(y) #int toplama işlemi

print(toplam1)
print(toplam2)


x = float(x)
print(x)

z=3.4
z = int(z)
print(z)
print(type(z))

isOnline = True
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

isOnline = True
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))

# seçili metinlerin hepsini yorum satırı yapmak için ctrl+k+c geri almak için ctrl+z
# '''yorumlar''' veya """yorumlar"""

pi = 3.14

r = float(input("yaricap: "))
alan = pi * (r ** 2)
cevre = 2 * pi * r
print("alan:",alan)
print("cevre:",cevre)
