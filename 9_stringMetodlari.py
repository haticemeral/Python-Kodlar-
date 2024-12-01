message = 'hello there. my name is sadık turan'

message = message.upper() #tüm harfleri büyük yapar
message = message.lower() #tüm harfleri küçük yapar
message = message.tittle() #tüm kelimelerin ilk harfini büyük yapar
messsage = message.capitalize() #stringin sadece ilk harfini büyük yapar
message = message.strip() # karakter dizisinin baş ve sondaki boşluk karakterlerini siler 
message = message.split() #karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar
#içine parametre vermeyince her kelimeyi bir dizi elemanı gibi görür
mesage = ' '.join(message) #ayrılmış ifadeleri arasına ' ' koyarak tekrar birleştirir
index = message.find('sadık') # string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa exception (-1) döndürür
print(index)
isFound = message.startsWith('B') #karakter dizisinin verilen parametre ile başlayıp başlamadığını kontrol eder.True  ya da false bi değer döndürür
print(isFound)
isFound = message.endsWith('n') #karakter dizisinin verilen parametre ile bitip bitmediğini kontrol eder.True  ya da false bi değer döndürür
print(isFound)
message = message.replace('sadık','çınar') #gönderilen ilk parametreyi dizi içinde bulup ikinci parametre ile değiştirir
message = message.replace('ç',  'c').replace('Ö', 'O') #bir metindeki türkçe karakterleri silip düzeltme işlemi, çoklu şeklde kullanılabilir
message = message.center(100) #String’i belirtilen değer kadar boşluk veya tercihen herhangi bir karakter ile ortalar. Belirtilen değer dizenin uzunluğundan kısa ise değişiklik yapılmaz
message = message.center(50, '*')


print(message)