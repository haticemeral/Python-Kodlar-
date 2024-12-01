#import datetime =>tüm metodları içerir
#tarih ve saat sınıfını içerir

from datetime import datetime
result = datetime.now()#şu anın bilgisini verir gün ay yıl saar dakika saniye
result = datetime.now().day #sadece gün bilgisi
simdi =  datetime.now() #simdi değişkeninin içine atadık
result = simdi.year #artık bu şekilde ulaşabiliriz
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi) #daha açıklayıcı
result = datetime.strftime(simdi,'%Y') #yıl
result = datetime.strftime(simdi,'%X') #saat
result = datetime.strftime(simdi,'%d') #gün
result = datetime.strftime(simdi,'%A') #gün string olarak
result = datetime.strftime(simdi,'%B') #ay string olarak
result = datetime.strftime(simdi,'%Y %B %A') #yan yana kullanılabilir

result = datetime.today()

t = '21 nisan 2023'
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)

t1 = '15 april 2023 hour 10:12:30'# bunu ekrana ayrı ayrı yazdıralım
dt = datetime.strftime(t1, '%d %B %Y hour %H:%M:%S')
print(dt)
dt = dt.year #belli birimlere ulaşabiliriz

birthday = datetime(2003,3,23,6,30,30)
result = datetime.timestamp(birthday)#saniye cinsinden hesaplar
result = datetime.fromtimestamp(result)#saniye verilmiş result değerini tarihe çevirir

result = simdi - birthday #yaşı bulmak için

from datetime import timedelta
result = simdi + timedelta(days=10,minutes=30) #bugünün tarihine 10 gün dakikaya 30 ekler
result = simdi - timedelta(days=10) #bugünün tarihinden 10 gün çıkarır



print(result)