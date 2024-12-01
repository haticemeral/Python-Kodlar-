import requests
import json
result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text) #adres üzerinden gelen json bilgiler konsola yazdırılır ayrıca json a çevirdik
#print(result[0]["title"])#üst satırda json çevirisi yaptığımız için bu şekilde kullanabildik
#print(result[0])

for i in result:
    if i["userId"]==1:#şart koyup filtreleyebiliriz
        print(i["title"])#sadece title olan bilgiler gelir




print(result)#<Response [200]> çıktısı başarılı bir sonucun geldiğini söyleyen kod
print(type(result)) #tipi str dir


