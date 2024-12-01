# iki seriyi toplarsak bir data frame oluşur(tek sütunlu iki tabloyu birleştirip tablo yapmak gibi)
import pandas as pd

#satır ve sütun bilgileri liste şeklinde yazılarak oluşturulabilir
df = pd.DataFrame([["ahmet",50],["ali",60],["yağmur",70],["çınar",80]])
#dataları ayrı tanımlayıp bir değişken içine atalım
data =[["ahmet",50],["ali",60],["yağmur",70],["çınar",80]]
df = pd.DataFrame(data, index=[1,2,3,4], columns=["name","grade"],dtype=float)#kolonlara isim verdik, indeks numaralarını kendimiz belirledik(normalde 0 dan başlar) ve tipini float yaptık
print(df)


#datalar dict biçiminde yazılarak da oluşturulabilir
dict = {"name":["ahmet","ali","yağmur","çınar"], "grade":[50,60,70,80]}
df = pd.DataFrame(dict, index=["212","232","236","456"]) #indeks numarasını öğrenci no gibi kullandık
print(df)


#json veri şeklinde yazıp da kullanabiliriz
dict_list =[
                {"name":"ahmet","grade":50},
                {"name":"ali","grade":60},
                {"name":"yağmur","grade":70},
                {"name":"çınar","grade":80},
            ]
df = pd.DataFrame(dict_list)
print(df)



s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data) #dataframe ile brileştirdik




print(df)

