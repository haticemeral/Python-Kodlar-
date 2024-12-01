import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns=["columns1","columns2","columns3"])

result = df
result = df["columns1"] #columns1 i getirir
result = type(df["columns1"]) #tipi seridir
result = df[["columns1","columns2"]] #yazılan columnsları aynı anda alır ve getirir


#satıra göre seçme(tipi seridir)
result = df.loc["A"] #  A satırındaki bilgileri liste olarak gönderir

# indekse göre seçme loc["row", "column"]
#sadece satır seçmek için loc["row"]
#sadece sütun seçmek için loc[: ,"column"]
result = df.loc[:,"columns1"]
result = df.loc[:, ["columns1","columns2"]]
result = df.loc[:, "columns1":"columns3"]# tüm satırları alır sütun olarak columss1 den columns3 e kadar alır ve getirir(başlangıç ve bitişler dahil)
result = df.loc[:, :"columns3"]# tüm satırları alır sütun olarak ilk sütundan columns3 e kadar alır ve getirir(başlangıç ve bitişler dahil)
result = df.iloc[2]#2. indeksteki satırı getirir

#hücreyi seçme
result = df.loc["A","columns1"]
result = df.loc["C","columns2"]
result = df.loc[["A","B"],"columns2"]#hem A daki hem de B deki columns2 deki hücrelerde bulunan bilgileri getirir
result = df.loc[["A","B"],["columns2","columns1"]]#belirtilen hücrelerdeki bilgileri getirir(çoklu hücre seçmek)



#yeni sütun ekleme
df["columns4"] = pd.Series(randn(3),["A","B","C"]) #yeni sütun dataframe e eklenir
df["columns5"] = df["columns1"] + df["columns3"]#yeni sütun 1 ve 3ün toplamı olarak yazdırılır(adı columns5 olur ve dataframe in sonuna eklenir)

#sütun silme
result2 = df.drop("columns5",axis=1)#axis değeri verilmezse hata verir axis değeri 1 sütun ise ,0 ise satırdır
#silinse orjinal df den silinmez
print(result2)

# result = df.drop("columns5", axis=1, inplace=True) İNPLACE TRUE YAPILIRSA ORJİNAL DF Yİ DEĞİŞTİRİR

print(result)

