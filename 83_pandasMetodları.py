import pandas as pd
import numpy as np

data ={
    "column1":[1,2,3,4,5],
    "column2":[10,20,20,40,50],
    "column3":["abc","bca","ade","cba","dea"]
}

df = pd.DataFrame(data)

result = df
result = df["column2"].unique()#column2 deki tekrarlamayan bilgileri getirir
result = df["column2"].nunique()#column2 deki tekrarlamayan bilgileri sayar ve sayısını getirir
result = df["column2"].value_counts()#column2 deki bilgileri sayar ve tekrar etme sayısını getirir

result = df["column1"]*2 #column1 deki tüm değerleri iki ile çarpar


def kareal(x):
    return x*x
result = df["column1"].apply(kareal) #parametre olarak fonksiyon alır ve fonksiyonu çalıştırır


kareal2 = lambda x: x*x #lambda fonksiyonu
result = df["column1"].apply(kareal) #parametre olarak fonksiyon alır ve fonksiyonu çalıştırır
result = df["column1"].apply(lambda x:x*x) #parametre olarak lambda fonksiyon alır ve fonksiyonu çalıştırır


result = df["column3"].apply(len)#column3 teki stringlerin uzunluklarını yazar

result = df.info #bilgi verir
result = df.sort_values("column2")#column2 deki sayıları sıralar
result = df.sort_values("column3")#column3 deki sitringleri alfabetik sıraya göre sıralar
result = df.sort_values("column3",ascending=False)#column3 deki sitringleri alfabetik sıranın tersine göre sıralar




print(result)