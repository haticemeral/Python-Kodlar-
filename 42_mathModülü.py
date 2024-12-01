# MATH MODÜLÜ
#1. yöntem
import math #math mdülünü dahil ettik içerdiği fonksiyonları kullanabiliriz

value = math.sqrt(49) #verilen parametrenin karekökünü alır
print(value)
value = math.factorial(5) #verilen paramettrenin faktöriyelini alır
print(value)
value = math.floor(5.9) #verilen parametreden küçük en büyük tam sayıyı verir
print(value)
value = math.ceil(5.9) #verilen parametreden büyük en küçük tam sayıyı verir
print(value)

import math as islem #artık math modülüne islem adıyla erişebiliriz
value = islem.factorial(5)

#2. yöntem
from math import * #math modülündeki tüm(*) fonksiyonları 
value = factorial(5) #üst satırda yaptığımız import iişlemi sayesinde böyle kullanabildik
print(value)
value = sqrt(9)
print(value)

#diğer kullanım
#sadece birkaç fonksiyon gerekli ise
from math import factorial,sqrt
value = factorial(5) #üst satırda yaptığımız import iişlemi sayesinde böyle kullanabildik
print(value)
value = sqrt(9)
print(value)
#value = ceil(9) import etmediğimiz için kullanamayız

#ilgili dosyadan alınan aynı isimli fonksiyoonlardan hangisi en son yazılmışsa o çalışır
from math import sqrt #bu tanımlamanın ardından def sqrt geldiği için yeni tanımlanan sqrt çalışır.bu satırın üstünde def sqrt tanımlanmış olsaydı hazır sqrt çalışırdı
value = sqrt(9)
def sqrt(x):
    print('X:'+ str(x))
print(value) #hazır sqrt çalışsaydı 3 yazardı bizim yazdığımız sqrt en sonda olduğu için o çalıştı ve 9 yazdı
