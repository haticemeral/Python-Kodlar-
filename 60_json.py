#cihazlar arasında ortak bir veri taşıma objesidir

#dictinary
person = {"name":"ali", "languages":["python","c#"]}
result = person["name"] #çıktısı ali olur
result = person["languages"] #çıktısı ["python","c#"] olur
result = person["languages"][0] #çıktısı python olur

#json dictinary gibi yazılır ancak ' ' arasına yazılır ve string gibi görünür
import json
person_string = '{"name":"ali", "languages":["python","c#"]}'
#! json string to dict
result = json.loads(person_string) #loads metdou ile json u dict çevirdik

result = result["name"]#çıktısı ali olur
result = result["langıages"]

with open("person.json") as f: #person.json u dahil ettik
    data = json.load(f)
    print(data)#dosya içindeki bilgileri okur ve yazdırır
    print(data["name"]) #bilgilere tek tek ulaşabilriz
    print(data["languages"])


#! dict to json string
person_dict = {
    "name": "ali",
    "languages": ["python", "c#"]
}
result = json.dumps(person_dict) #dumbs metodu ile dict i json a çevirdik

with open("person2.json", "w") as f: #yazma modunda açtık
    json.dump(person_dict, f) #person.dict içindeki bilgileri f içine yazdırır


#**person_string i dictinary i ye çevirelim
person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)#düzenli yazdık
print(result)
print(person_dict)


print(result)

