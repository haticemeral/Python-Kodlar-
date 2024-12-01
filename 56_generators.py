# generator bellekte yer kaplamayan iterator üretir
def cube():
    result = []
    for i in range(5):
        result.append(i**3)
    return result

print(cube())
# 5 sayı için bu kodun çalışması bellek için zor değildir ancak 50000 sayının çalıştırılması bellekte gereksiz yer kaplar bunun için generator kullanabiliriz

def cube():
    for i in range(5):
        yield i ** 3 #yield anahtar kelimesi ile istenen işlem yapılır ancak bellekte tutulmaz ya da saklanmaz

iterator = cube() #iteratör hale getirdik

#uzun yol
# print(next(iterator))  #0      
# print(next(iterator))  #1    
# print(next(iterator))  #8    
# print(next(iterator))  #27    
# print(next(iterator))  #64
# print(next(iterator)) #StopIteration hata mesajı gönderir   

#kısa yol
for i in iterator:
    print(i) #StopIteration mesajını vermez

#daha kısa yolu
"""
#iterator = cube() yazmadan 
for i in cube():
    print(i)
"""

liste = [i**3 for i in range(5)] #bu kullanımda 0 dan 5 e kadar küp alıp yazdırır
print(liste)

liste = (i**3 for i in range(5)) #bu kullanımda ise 0 dan 5 e kadar küp alıp yazdırır ancak generator olarak yapar yani hafızada tutulmaz
print(liste)
for i in liste:
    print(i)
