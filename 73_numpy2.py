import numpy as np

result = np.arange(1,10)#1den 10a kadar bir dizi oluiturur
result = np.arange(10,100,3)#10dan 100e kadar üçer üçer giden dizi
result = np.zeros(10)#10 elemeanlı her elemanı sıfır olan dizi(float)
result = np.ones(10)#10 elemanlı her elemanı bir olan dizi(float)
result = np.linspace(0, 100, 5)#0 ve 100 arasını 5 eşit parçaya böler ve dizi oluşturur(float)
result = np.random.randint(0, 10)# 0 dahil 10 dahil değil bu aralıkta rastgele bir sayı üretir(sadece üst değer de verilebilir program başlangıcı 0dan alır)
result = np.random.randint(0, 10, 3)# 0 dahil 10 dahil değil bu aralıkta rastgele 3 sayı üretir(sadece üst değer de verilebilir program başlangıcı 0dan alır)
result = np.random.rand(5)# 0 ile 1 arsaında 5 sayı üretir
result = np.random.randn(5)# -1 ile 1 arasında 5 sayı üretir

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis=1))#matrisin satırları toplamını getirir
print(np_multi.sum(axis=0))#matrisin sütunları toplamını getirir

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()#üretilen dizideki en büyük değeri getirir 
result = rnd_numbers.min()#üretilen dizideki en küçük değeri getirir 
result = rnd_numbers.mean()#üretilen dizideki sayıların ortalamasını getirir (float)
result = rnd_numbers.argmax()#üretilen dizideki en büyük değerin indeksini getirir 
result = rnd_numbers.argmin()#üretilen dizideki en küçük değerin indeksini getirir 



print(result)



#! NUMPY DİZİLERİNDE İNDEKSLERE ULAŞMAK

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75])
result = numbers[5]#5 indekteki değeri getirir
result = numbers[-1]#sonuncu elemanı getirir
result = numbers[0:3]#0 ile 3. indis arasındaki(3. indis dahil değil) elemanları getirir(0 belirtilmeden (:3)yazılması da aynı anlama gelir)
result = numbers[3:]#3. elemandan sonuncu elemana kadar yazdırır
result = numbers[:]#tüm listeyi yazdırır
result = numbers[:-1]#tüm listeyi tersten yazdırır

numbers2 = np.array([0,5,10],[15,20,25],[50,75,85])
result = numbers2[0]#matrisin  0. indeksini getirir [0,5,10]
result = numbers[0,2]#matrsin 0. indisindeki satırın 2. indisteki sutünundaki elemanı getirir 
result = numbers2[:]#tüm satırları seçer
result = numbers2[:2]#tüm satırlarda 2. indisin sütunundaki değerleri geitirir [10,25,85]
result = numbers2[:,0:2]#tüm satırları seçer ve 0. indisten 2. indise kadar olan değerlerle yeni bir matris oluşturur(0 dahil 2 dahil değil)


print(result)

arr1 = np.arange(0.10)
arr2 = arr1 #referans kopyalaması
arr2[0] = 20 #iki dizide de 0. indis değiştirilir

"""
copy fonksiyonuyla kopyalama yapılırsa herhangi bir değişkende yapılan atama ya da değiştirme işlemi sadece o fonksiyonu etkiler
arr2 = arr1.copy() 
arr2[0] = 20
"""

print(arr1)
print(arr2)



#! matematiksel işlemler ve fonksiyonlarla beraber numpy kullanımı

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
print(numbers1)
print(numbers2)

result = numbers1 + numbers2 #iki dizinin aynı indisteki elemanlarını toplar ve yeni bir dizi içinde gruplama yapar
result = numbers1 + 10 #her bir eleman üzerine 10 ekler

result = numbers1 - numbers2 #iki dizinin aynı indisteki elemanlarını çıkarır ve yeni bir dizi içinde gruplama yapar
result = numbers1 - 10 #her bir elemandan 10 çıkarır(negatif olabilir)

result = numbers1 * numbers2 #iki dizinin aynı indisteki elemanlarını çarpar ve yeni bir dizi içinde gruplama yapar
result = numbers1 * 10 #her bir elemanı 10 ile çarpar

result = numbers1 / numbers2 #iki dizinin aynı indisteki elemanlarını böler ve yeni bir dizi içinde gruplama yapar(float)
result = numbers1 / 10 #her bir elemanı 10a böler

result = np.sin(numbers1)#tüm değerlerin sin değerini alır(float türündedir ve negatif olabilir)
result = np.cos(numbers1)#tüm değerlerin cos değerini alır(float türündedir ve negatif olabilir)
result = np.sqrt(numbers1)#tüm değerlerin karekök değerini alır(float türündedir)

#dizileri çok boyutlu dizi haline getirelim
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2))#matrisleri dikey birleştirir
result = np.hstack((mnumbers1,mnumbers2))#matrisleri yatay birleştirir

result = numbers1 >= 5 #elemanlar 5 ten büyükse o elemanlar için true, olmayan eleemanlar için false değeri dönerek liste gibi yazdırılır
result = numbers1 % 2 == 0#çift elemanlar için true, tek elemanlar için false değeri dönerek liste şeklinde yazdırır



print(result)

