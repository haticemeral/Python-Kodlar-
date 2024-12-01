maasAli = 5000 #yeni değişken
maasAhmet = 4000 #diğer değişken
vergi =0.27 #diğer değişken
print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))
#Değişken tanımlama kuralları
#rakam ile başlamaz
#ilk değeri atamamız gerekir
#büyük küçük harf duyarlılığı vardır
#türkçe karakter kullanılmaz
#boşluk olamaz ama _ olabilir

yas = 20 #int
_age = 20 #int
x = 1 #int
y = 2.0 #float
name = "cinar" #string
isStundent = True #bool
a = 10
b = 20
print(a+b) #30
c = "10"
d = "20"
print(c+d) #1020 string birleştirme işlemi

x, y, name, isStundent = (1, 2.3, "cinar", True) #tek satırda atama

number1 = 10 # ilk değer ataması
print(number1) # ekrana yazdırma
number1 = 20 # ikinci değer ataması
print(number1) #ekrana yeni atanan değerin yazdırılması
number1 += 30 #değere 30 eklendi
print(number1) #ekrana yeni atanan değerin yazdırılması
number1 -= 10
print("yeni deger:", number1) #ekrana yeni atanan değerin yazdırılması
