import pandas as pd
data = pd.read_csv("nba.csv") #parametre olarak verilen dosyadan bilgileri okur

data.dropna(inplace=True) #yapılan değişiklikleri kaydetme
data["name"] = data["name"].str.upper()#hepsini büyük harfe çevirir
data["name"] = data["name"].str.lower()#hepsini büyük harfe çevirir

data["index"] = data["name"].str.find("a")#yeni bir kolon ekler ve içinde kaç a harfi olduğunu sayıp oraya yazar eğer hiç yoksa -1 yazar
data = data[data.Name.str.contains("jordan")]#jordan olan kayıtları getirir


print(data.head(10))#baştan 10 tanesini yazdır