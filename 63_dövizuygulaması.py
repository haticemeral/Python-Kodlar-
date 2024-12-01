import requests
import json

api_url = "https://api.exchangeratesapi.io/lastest?base="
bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz "))

result = requests.gets(api_url+bozulan_doviz)
result = json.loads(result.txt) #json bilgiye çevirdik

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"[alinan_doviz]],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))