import pandas as pd
import numpy as np
#data (heterojen yapıda olabilir)
numbers = [1, 2, 3, 4]
letters = ["a", "b", "c", "d"]
a = ["a", "b", "c", 30]
dict = {'a':10, 'b':20, 'c':30, 'd':40} 
random_numbers = np.random.randint(10,100,6) #10 ile 100 arasında rastgele 6 tane sayı üretir

#indeks numarası verilerek ekrana yazılmış olur
pandas_series = pd.Series() #tek boyutlu bir dizi (float)
pandas_series = pd.Series(numbers) #int
pandas_series = pd.Series(letters) #string
pandas_series = pd.Series(a) #object
pandas_series = pd.Series(5,[0,1,2,3]) #int tipinde 0 dan 3. indekse kadar 5 değeri verilip yazdırılır
pandas_series = pd.Series(numbers,['a','b','c','d']) #her indekse karşılık indeks olarak a b c d değerlerini verir karşıda da numbersın değerlerini yazdırır
pandas_series = pd.Series(dict) #int
pandas_series = pd.Series(random_numbers) 


pandas_series = pd.Series([20,30,40,50], ['a','b','c','d'])

result = pandas_series[0]#0. indisteki elemana ulaşır (20)
result = pandas_series[-1]#son indisteki elemana ulaşır (50)
result = pandas_series[:2]#ilk iki elemana ulaşır
result = pandas_series[-2:]#sondan 2 elemana ulaşır
result = pandas_series['a']# a ya karşılık gelen elemana ulaşır
result = pandas_series[['a','c']]#a ya ve c ye karşılık gelen elemanlara ulaşır(olmayan bir data çağırılırsa örneğin 'e' gibi NaN mesajı verir)

result = pandas_series.ndim #kaç boyutlu olduğunu getirir
result = pandas_series.dtype #tipini  getirir
result = pandas_series.sum() #elemanların toplamı
result = pandas_series.max() #elemanlar içindeki max değeri getirir
result = pandas_series.min() #elemanlar içindeki min değeri getirir
result = pandas_series + 50 #her elemana 59-0 ekleyip yeni değeri getirir
result = pandas_series + pandas_series #her elemana karşılık gelen aynı indeksli değerleri toplar yani her değerin 2 katı getirilmiş olur
result = np.sqrt(pandas_series) #tüm elemanların karekökünü alır
result = pandas_series >= 50 #şartı sağlayan elemanlarıda true değeri sağlamayan elemanlarda false değeri döner




print(pandas_series)
print(result)
