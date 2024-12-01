import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["columns1","columns2","columns3","columns4","columns5"])
result = df

result = df.columns #sütun bilgileri liste şeklinde gelir
result = df.head(10) #ilk 10 satırı getirir(parametre verilmezse 5 tane getirir)
result = df.tail(10) #son 10 satırı getirir(parametre verilmezse 5 tane getirir)

#sütun seçme işlemi
result = df["columns1"].head() #columns1 in ilk 5 satırını getirir
result = df[["columns1","columns2"]].head() #çoklu sütun seçilir(parametre olarak yazılan sütunlar) ilk 5 satırı getirir
result = df[5:15] #parçalama işlemi 5 ile 15 arası olan satırları getirir
result = df[5:15][["columns1","columns2"]].head() #satır olarak 5 ile 15 arası sütun olarak columns1 ve columns2 de bulunanları getirir

#filtreleme
result = df>50 #50 den büyyük olan hücrelere true küçük olan hücrelere false değeri yazar
result = df[df>50] #50 den büyyük olan hücrelere true küçük olan hücrelere NaN değeri yazar
result = df[df%2==0] #çift olan sayılara true tek olan sayılara NaN yazdırır


#istenilen kolon üzerinden filtreleme yapma
result = df["columns1"]>50 #50 den büyyük olan hücrelere true küçük olan hücrelere false değeri yaz
result = df[df["columns1"]>50] #sadece şartı sağlayan değerlerle yeni tablo yazdırır
result = df[df["columns1"]>50][["columns1","columns2"]] #sadece "columns1","columns2" deki değerlerde bulunan bilgiler için şartı kontrol eder ve şartı sağlayanları yenş bşr tablo ile yazdırır
result = df[(df["columns1"]>50) & (df["columns1"]<70)] #sadece şartı sağlayan değerlerle yeni tablo yazdırır
result = df[(df["columns1"]>50) | (df["columns2"]>60)] #sadece şartı sağlayan değerlerle yeni tablo yazdırır
result = df[(df["columns1"]>50) | (df["columns2"]>60)][["columns1","columns2"]] #columns1 ve columns2 den sadece şartı sağlayan değerlerle yeni tablo yazdırır
result = df.query("columns >=50 & columns%2==0") #koşulu bu şekilde de yazabiliriz
result = df.query("columns >=50 & columns%2==0")[["columns1","columns2"]] #sadece columns1 ve columns2 kontrol eder 


print(result)