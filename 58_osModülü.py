import os

result = os.name #işletim sistemini getirir

result = os.getcwd #dosyanın hangi klasörde olduğunu gösterir

#dizin değiştirme
#os.chdir() ile (change directory) farklı bir klasör içerisine geçebilirsiniz
os.chdir('..') # otomatik olarak c: içine gider

#klasör oluşturma
# os.mkdir("newdirecoty")
# os.makedirs("C:\\newdirectory/yeniklasör")

#listeleme
#os.listdir() ile hangi klasördeyseniz onun içerisindeki dosya ve klasörleri döndürür
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'): #sadece .py uzantılı dosyaları gösterir
#         print(dosya)

#dosyanın oluşma zamanı
import datetime
result = os.stat("_datetime.py")
result = datetime.datetime.fromtimestamp(result.st_ctime)#oluşturulma zamanı
result = datetime.datetime.fromtimestamp(result.st_attime)#son erişilme zaamanı
result = datetime.datetime.fromtimestamp(result.st_mtime)#değiştirme zamanı

#Eğer bulunduğunuz klasör içerisinde yeni bir klasör oluşturmak isterseniz os.mkdir() methodunu kullanılır
#os.rename("aa","yeniKlasor") ile aa olan klasör adını yeniKlasor adıyla değişilir
#rmdir() içi boş olan bir klasörü silmek için kullanılır
#stat() Herhangi bir dosyanın boyutu, değiştirilme tarihi gibi bilgileri döndürür.
#walk() Verdiğiniz bir klasörün altındaki dizinleri ve dosyaları görebileceğiniz bir method.
#path() Bir dosya ve klasörün var olup olmadığını kontrol etmek istediğinizde path.exists() methodunu kullanabilirsiniz
#Verdiğiniz parametrenin bir dizin mi yoksa dosya mı olduğunu da sorgulayabilirsiniz. Bunun için ise path.isdir() ve path.isfile() methodlarını kullanıyoruz




print(result)