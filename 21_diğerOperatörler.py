#identity operator: is (adreslere bakar)
x = y = [1, 2, 3] #referansları aynı olan x ve y listeleri
z = [1, 2, 3] #içeriği aynı olan ancak referansı farklı olan z listesi

print(x==y) #true
print(x==z) #true
print(x is y) #true
print(x is z) #false
print(x is not z) #true

#membership operator: in (içeip içermediğini kontrol eder)
x = ["apple", "banana"]
print("banana" in x) #true

name = "çınar"
print('a' in name) #true
print('b' in name) #false
print('b' not in name) #true