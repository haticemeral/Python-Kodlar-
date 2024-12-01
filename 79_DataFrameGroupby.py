import pandas as pd
import numpy as np
personeller = {
    'çalışan':['ahmet yılmaz','can ertürk','hasan korkmaz','cenk saymaz','ali turan','rıza ertürk','mustafa can'],
    'departman':['insan kaynakları','bilgi işlem','muhasebe','insan kaynakları','bilgi işlem','muhasebe','bilgi işlem'],
    'yaş':[30,25,45,50,23,34,42],
    'semt':['kadıköy','tuzla','maltepe','tuzla','kadıköy','tuzla','maltepe'],
    'maaş':[5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["maaş"].sum() #gruplama yapmadan maaşları toplar

result = df.groupby("departman").groups #departmanları gruplar
result = df.groupby( ["departman","semt"]).groups #depertmanı ve semti aynı olanları gruplar


for name,group in df.groupby("semt"): #semtlere göre gruplar oluşturup isimleriyle beraber yazar
    print(name)
    print(group)


for name,group in df.groupby("departman"): #departmana göre gruplar oluşturup isimleriyle beraber yazar
    print(name)
    print(group)

result = df.groupby("semt").get_group("kadıköy") #semti kadıköy olanları gruplar
result = df.groupby("departman").get_group("muhasebe") #departmanı muhasebe olanları gruplar

#? alınan gruplar üzerinde işlem yapma
result = df.groupby("departman").sum() #departmanların ayrı ayrı yaşlarının ve maaşlarının toplamlarını yazdırır
result = df.groupby("departman").mean() #departmanların ayrı ayrı yaşlarının ve maaşlarının ortalamalarını yazdırır
result = df.groupby("departman")["maaş"].mean() #departmanların maaşlarının ortalamalarını yazdırır
result = df.groupby("departman")["yaş"].mean() #departmanların yaşlarının ortalamalarını yazdırır
result = df.groupby("semt")["yaş"].mean() #semtlere göre yaşların ortalamalarını yazdırır
result = df.groupby("semt")["çalışan"].count()#semtlere göre çalışan sayısı
result = df.groupby("departman")["yaş"].max() #departmanlara göre yaşlardan en büyüğünü yazdırır
result = df.groupby("departman")["maaş"].min() #departmanlara göre maaşların en az olanını yazdırır


result = df.groupby("departman")["maaş"].min()["muhasebe"] #departmanlardan sadece muhasebe içinden maaşların en az olanını yazdırır

result = df.groupby("departman").agg(np.mean) #her depertman için yaş ve maaş ortalaması alır
result = df.groupby("departman")["maaş"].agg([np.sum,np.mean,np.max,np.min]) #her depertmanın maaşının sırasıyla toplamını ortalamasını max değerini ve min değerini yazdırır
result = df.groupby("departman")["maaş"].agg([np.sum,np.mean,np.max,np.min]).loc("muhasebe") #muhasebe depertmanının maaşının sırasıyla toplamını ortalamasını max değerini ve min değerini yazdırır




print(result)