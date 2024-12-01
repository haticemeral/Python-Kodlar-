name = 'sadık turan'

for letter in name:
    if letter =='a':
        break #şart sağlandığında kodu kırıp bloktan çıkar
    print(letter)
#çıktısı=>s

for letter in name:
    if letter=='a':
        continue #şart sağlandığında kod bloğunu çalıştırmadan diğer koşula geçip devam eder
#çıktısı=>sdık turn

x = 0
while x<5:
    if x==2:
        break
    print(x)
    x+=1
#çıktısı=> 0 1

x = 0
while x<5:
    x+=1
    if x==2:
        continue
    print(x)
#çıktısı=> 0 1 3 4 5




