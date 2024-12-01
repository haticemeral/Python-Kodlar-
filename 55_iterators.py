liste = [1, 2, 3, 4, 5]
#iteratörler ile liste elemanlarının üstünde tek tek dolaşabiliriz
iterator = iter(liste) #bir iteratör oluşturduk(for döngüleri kendiliğinden iteratördür)

print(next(iterator))# listedeki 1 elemanını yazdırır
print(next(iterator))# listedeki 2 elemanını yazdırır
print(next(iterator))# listedeki 3 elemanını yazdırır
print(next(iterator))# listedeki 4 elemanını yazdırır


#listedeki eleman sayısından fazla kez next metodunu çağırırsak  StopIteration hata mesajını verir

for i in liste:
    print(i)

#for un çalışma mantığı
iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break



class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        

list = MyNumbers(10,20)
#for döngüsü ile yazdırma
# for x in list:
#     print(x)

#for döngüsü kullanmadan yazdırma
myitter = iter(list)
print(next(myitter))#bundan 50 oluncaya kadar ayrı ayrı yazarız 51 olunca bize hata mesaı gönderir ve durur
# 2. yol
while True:
    try:
        element = next(myitter)
        print(element)
    except StopIteration:
        break
