webSite = "http://www.sadikturan.com"
course = "python kursu: baştan sona python programlama rehberiniz (40 saat)"

#1- karakter dizilerinin kaç karakter olduğunu bulunuz
result = len(course)
lenght = len(webSite)
print(result)
#2- website içinden www karakterlerini alın
result = webSite[7:10]
print(result)

#3- website içinden com karakterlerini alın
result = webSite[22:25]
result = webSite[lenght-3:lenght]

#4-course içinden ilk 15 ve son 15 karakterlerini alın
result = course[0:15]
print(result)
result = course[:15]
print(result)
result = course[-15:65]
print(result)

#5-course ifadesindeki karakterleri tersten yazdıralım
result = course[::1] #tüm ifadeyi alır ve yazdırır :: şeklinde de yazabilirdik
result = course[::-1] # tersten yazdırır
# adım sayısı için ek bilgi
s = '12345' * 5 #stringi 5 kez terkrarlatır
print(s[::5]) # her 5 karakterde bir kere print çalışır ve 11111 yazdırır


name, surname, age, job = 'bora', 'yıllmaz', 32, 'mühendis'
#6- yukarıda verilen değişkenler ile ekrana aşağıdakş şfadeyş yazdırın
#  'benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis'
result = "benim adım " + name + " " + surname + ", yaşım " + str(age) + " ve mesleğim " + job
result = 'benim adım {} {}, yaşım {} ve mesleğim {}'.format(name, surname, age, job)
result = f'benim adım {name} {surname}, yaşım {age} ve mesleğim {job}'

#7- 'hello world' ifadesindeki w harfini W harfi ile değiştirin
s = 'helo world'
s = s[0:6] + 'W' + s[-4:]

s.replace('w', 'W') #diğer yol

#8- 'abc' ifadesini yan yana 3 defa yazdırın
result = 'abc ' * 3
  
