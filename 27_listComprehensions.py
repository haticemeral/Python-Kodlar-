#aşağıdaki iki kod aynı işi yapar
#0dan 10a kadar olan sayıları numbers listesine ekler ve yazdırır
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

numbers = [x for x in range(10)]
print(numbers)

#aşağıdaki iki kod aynı işi yapar
#0dan 10a kadar olan sayıların karesini alıp yazdırır
for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)

#1den 10a kadar olan sayılardan 3e bölünenleri karesini alır
numbers = [x**2 for x in range(10) if  x%3==0]
print(numbers)

#aşağıdaki iki kod aynı işi yapar
#stringin her harfi ile yeni bir liste oluşturur
myString = 'hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

#yaşları hesaplar
years = [1993, 1999, 2008, 1956, 1986]
ages = [2023-year for year in years]
print(ages)

#1den 10a kadar olan sayıları çift ise result listesine atar tek ise tek yazdırır ve listeyi çıktı verir
result = [x if x%2==0 else 'tek' for x in range(1,10)]
print(result)

#aşağıdaki iki kod aynı işi yapar
#0 dan 3e kadar döngü şartlarına göre önceden boş olan result listesine atar ve yazdırır
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)


