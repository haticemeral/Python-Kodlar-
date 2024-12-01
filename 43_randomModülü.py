# RANDOM MODÜLÜ
import random

result = random.random() #0.0 ile 1.0 arasında rastgele bir sayı üretir

result = random.random() * 100 #üretilen sayılar 100 ile çarpılır

result = int(random.uniform(10,100)) #10 ile 100 arasında integer bir değer oluşturur

result = random.randi(1,100) #parametre olarak gönderilen sayıların aralığında rastgele bir sayı oluşturur

names = ['ali', 'yağmur', 'deniz', 'cenk']
result = names[random.randit(0,len(names)-1)]

result = random.choice(names) #names içinden bir eleman seçip getirir


greeting = 'hello there'
result = random.choice(greeting) #string içinden rastgele bir harf getirir

liste = list(range(10)) #1 den 10a kadar olan bir liste oluşturur
random.shuffle(liste) #aralık içinde rastgele sırada gelir
ressult = liste

liste = range(100) #100e kadar değerler bulunur
result = random.sample(liste,3) #verilen listeden rastgele 3 değer getirir
result = random.sample(names,2)#names listesinden rastgele 2 ad getirir


print(result)
