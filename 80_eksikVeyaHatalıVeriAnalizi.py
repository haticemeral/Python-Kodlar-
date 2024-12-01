import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=['a','c','e','f','h'], columns=['columns1','columns2','columns3'])

df = df.reindex(['a','b','c','d','e','f','g','h','g'])#daha önceden verilmemiş indexler(b,d,g) için NaN değeri atanır ve yeni tablo oluşturulur

result = df

result = df.drop("columns1", axis=1) #columns1 sütununu siler
result = df.drop(["columns1","columns2"], axis=1) #columns1 ve columns2 sütununu siler
result = df.drop("a", axis=0) #a satırı silinir
result = df.drop(["a","b","h"], axis=0) #a,b ve h satırı silinir

#kolon ekleyip hücrelere bilgi atama
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["columns4"] = newColumn


#bilgi içermeyen NaN hücreler
result = df.isnull() #NaN değerlere karşılık gelen hücrelerde true değeri, diğer hücrelerde false değeri yazar
result = df.notnullnull() #NaN değerlere karşılık gelen hücrelerde false değeri, diğer hücrelerde true değeri yazar

result = df.isnull().sum() #her kolondaki NaN değerleri sayar
result = df["columns1"].isnull().sum() #columns1 kolonundaki NaN değerleri sayar
result = df[df.isnull().sum()] #columnslardaki NaN değerleri tablo şeklinde gelir


result = df.dropna()#içinde NaN değer olan satırları siler(axis değeri varsayılan olarak sıfırdır)
result = df.dropna(axis=1)#içinde NaN değer olan sütunları siler(axis değeri 1 yaptık)
result = df.dropna(how="any")#en az bir tane NaN varsa o satırı siler
result = df.dropna(how="all")#tüm değerleri NaN ise o satırı siler
result = df.dropna(subset=["columns1","columns2"],how="any")#columns1 ve columns2 yi kontrol edip içinde nan olan değerleri siler
result = df.dropna(thresh=2)#nan dışında en az iki bilgi girilmiş kayıtları silmez

#nan değerlere bilgi yok yazma
result = df.fillna(value="no input")
result = df.fillna(value=1)#nan olan yerlere 1 yazar

#toplamı ve ortalamayı bulan fonksiyon(nan değerler hariç)

result = df.sum()#kolonların ayrı ayrı toplamı
result = df.sum().sum()#tüm değerlerin toplamı
result = df.size()#toplam eleman sayısı 
result = df.isnull().sum()#kolonlardaki nan değerlerin sayısı
result = df.isnull().sum().sum()#tüm nan değerlerin sayısı
def ortalama(df):
    toplam = result = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value=ortalama(df))


print(result)
print(df)
