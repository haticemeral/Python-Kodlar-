x, y, z = 5, 10, 20

x, y = y, x #x in içine y; y nin içine x in değeri atandı
print(x, y, z)

x = 5
x += 5 #x = x + 5
x -= 5 #x = x - 5
x *= 5 #x = x * 5
x /= 5 #x = x / 5
x %= 5 #x = x % 5
y = 10
y //= 5 #y = y // 5
y **= 5 #y = y ** 5

values = 1, 2, 3 #tuple list
print(values)
print(type(values))
x, y, z = values #values içindeki değerleri x y ve z değişkenlerine atadık
#values içindeki değerler daha çok ya da daha az olsaydı hata alırdık örneğin x, y = values gibi

values = 1, 2, 3, 4, 5
x, y, *z = values #(1, 2, [3, 4, 5]) şeklinde atanır
print(x, y ,z[0]) #şeklinde yazılırsa 1, 2, 3 şeklinde çıktı alırız

print(x, y, z)


