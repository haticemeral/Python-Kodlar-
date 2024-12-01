# RANGE()
for item in range(10): #bitiş koşulu belirtilir
    print(item) #0 dan 10 a kadar yazdırır

for item in range(3,10): #başlangıç değeri de verilebilir
    print(item) #3 ten 10 a kadar yazdırır

for item in range(50,100,10): #artış miktarı da verilebilir
    print(item) #50 den 100 e kadar onar onar yazdırır

print(list(range(50,100,20))) #verilen koşullara göre bir liste yapar=>[50,70,90]

# ENUMERATE()
index = 0
greeting = 'hello'
for letter in greeting:
    print(f'index:{index} letter:{greeting[index]}')
    index += 1

#yukarıdaki kodu enumerate ile yazalım

greeting = 'hello'
for index,letter in enumerate(greeting):
    print(f'index: {index} letter:{letter}')


# ZIP()
list1 = [1, 2, 3, 4, 5] #birinci liste
list2 = ['a', 'b', 'c', 'd', 'e'] #ikinci liste
print(list(zip(list1,list2))) #iki listeyi kendi arasında eşleştirir

list3 = [100, 200, 300, 400, 500]
print(list(zip(list1,list2,list3))) #üç listeyi birbir eşleştirir

for item in zip(list1,list2,list3):
    print(item) #oluşturulmuş tuple listeleri sırasıyla yazdırır

for a,b,c in zip(list1,list2,list3):
    print(b) #b ye denk gelen kısımları yazdırır
    

for a,b,c in zip(list1,list2,list3):
    print(a,b,c) #liste şeklinde yazmaz 