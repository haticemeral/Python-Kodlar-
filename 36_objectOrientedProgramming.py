#Python ile Nesne Tabanlı Programlama
#Nesne Tabanlı Programlama gerçek hayattaki nesneleri yazılım dünyasına aktarma çabasıdır. Örneğin yeni bir araba üretecek bir firmayı düşünelim. Somut olarak üretilecek olan arabanın tüm özellik (attributes) ve fonksiyonlarını (method) ilk olarak yazılıma aktarmak gerekiyor. Bu aktarım aşamasının kendisi aslında arabanın tüm özellik ve fonksiyonlarını içerecek olan bir sınıfın (class) oluşturmasıdır. Sınıf tanımlanmasından sonra ise sınıfın tüm özellik ve yeteneklerine sahip olacak her kopyaya ise nesne (object) diyoruz.

#Nesne tabanlı programlama kapsamındaki kullandığımız terimler class (sınıf), object (nesne), attributes (özellik) ve metod kavramlarıdır.

#Class (Sınıf) Nedir ?
#Gerçek hayattaki bir nesneyi yazılım dünyasında temsil edecek olan yapıya class denir. Tabi ki bu terim nesne tabanlı programlamayı daha somut bir şekilde anlamamız için söyleyebileceğimiz bir açıklamadır.

#Biz zaten bu aşamaya kadar nesne tabanlı programlama ile alakalı bir çok sınıfı zaten kullandık. Örneğin, python ile birlikte gelen list, dict gibi yapıların bir class olduğunu zaten biliyoruz. Peki class bize ne fayda sağlar ?
#Örneğin; 
liste = [1,2,3]

print(type(liste))    # <class 'list'>
print(liste)          # [1, 2, 3]
#Burada tanımlanan bir listenin class olarak oluşturulması demek şimdi ve ileride tanımlanacak olan tüm list ismindeki class ların aynı özelliklere ve aynı yeteneklere sahip olmasıdır. Örneğin liste üzerine bir eleman eklemek için append() metodunu list sınıfı üzerinden çağırabiliriz yani buradaki append() metodunu kendimiz oluşturmak zorunda değiliz zaten hazır ve kullan hepsi bu kadar.

#Demek ki buradan anlıyoruz ki; bir kavramı class olarak oluşturmamız işleri daha sistemli ve kolay bir şekilde tertip düzene bağlı olarak yapmamızı sağlıyor. 

#Bazı sınıflar python içerisinde hazır olarak geliştiriciler tarafından hazırlanmış ve kullanımınıza sunulmuş tabi ki her işimizi halledecek sınıf python kütüphanesinde mevcut değil. Dolayısıyla bazı sınıfları kendimiz oluşturmalıyız örneğin bir araba sınıfı ya da öğrenci bilgilerini içerecek olan bir student sınıfı gibi.
#Örneğin;
class Araba:
    pass

#Object (Nesne) Nedir ?
#Nesne tabanlı programlama da bir nesneyi modellemek için ilk başta class oluşturuyoruz. Örneğin bir araba sınıfı ya da bir öğrenci sınıfı. Ve sınıfa ait tüm özellik ve fonksiyonları sınıf içerisine ekliyoruz.

#Örneğin araba sınıfı açısından düşünürsek arabanın vites tipi, yakıt tipi gibi arabayı temsil edecek olan özelliklerdir ve arabanın sahip olduğu yetenekler ise örneğin arabanın çalıştırılması, stop edilmesi, araç takip özelliği gibi.

#Temel sınıfa eklediğimiz özellik ve fonksiyonlar ile üzerinde çalışmak istediğimiz yapıyı tamamen yazılım tarafına aktarmış oluyoruz. Ve bir araç üretmek istediğimizde ise temel sınıfın kopyası gerekiyor. Çünkü her kopya üzerine ekleyeceğimiz her araca göre farklı bilgiler olmalıdır. Örneğin sınıfta aracın renk bilgisini içerecek bir özellik olmalı ancak özelliğe değer atama işi sınıftan kopyalanacak olan nesne üzerinden yapılmalıdır. Peki örneğimize daha yakından bakalım;

class Araba:
     def __init__(self, renk):
        self.renk= renk

kirmiziOpel = Araba("kırmızı")
maviOpel = Araba("mavi")
siyahOpel = Araba("siyah")
#Tanımladığımız Araba sınıfı içinde tanımlanan bir özellik aracın renk bilgisidir ve temel sınıftan türetilecek olan nesneler üzerinden ise renk alanına verdiğimiz değerler farklı olabilir. Dolayısıyla Araba sınıfından türettiğimiz 3 nesneden bahsedebiliriz. 

#Zaten python' da tanımladığımız bir list sınıfı aynen bu şekilde oluyor. Yani tanımlanan her bir liste içindeki elemanlar farklı ancak list sınıfı üzerinden yapabileceğimiz yetenekler ortaktır. Liste üzerine ekleme yapma, listeden eleman silme, listedeki eleman sayısını öğrenme gibi bir çok hazır yetenekler bize geliyor.

#Attributes (Özellik) Nedir ?
#Sınıf içinde tanımlanan sınıfın her hangi bir özelliğini taşıyacak olan değişkenlere verdiğimiz isimdir. Örneğin Arabanın renk bilgisi gibi.

class Araba:
     def __init__(self, renk):
        self.renk= renk
#Metod Nedir ?
#Sınıflara hizmet eden fonksiyonlara verilen isimdir. Örneğin bir Arabanın çalıştırılması, hızlandırılması, takip sistemi vb. fonksiyonlara verdiğimiz isim metod olarak adlandırılır.

class Araba:
     def __init__(self, renk):
        self.renk= renk

     def start(self):
         print("araç çalıştırıldı.")

     def stop(self):
         print("araç durduruldu.")

