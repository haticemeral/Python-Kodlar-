# with open("newfile","r+",encoding='utf-8') as file:
#     #r+ hem okuma hem de yazma işlemş yapar
#     file.seek(20)
#     file.write("deneme")#20. karakterden itibaren deneme yazar ve güncellemiş olur

# with open("newfile","r+",encoding='utf-8') as file:
#     #r+ hem okuma hem de yazma işlemş yapar
#     print(file.read())


#******sayfanın sonuna bilgi ekleme ve güncelleme
# with open("newfile","r+",encoding='utf-8') as file:
#     file.write("\nemel turan") 
# with open("newfile","r+",encoding='utf-8') as file:
#     print(file.read())


#******sayfanın başında bilgi ekleme ve güncelleme
# with open("newfile","r+",encoding='utf-8') as file:
#     content = file.read()
#     content = 'efe turan\n' + content #dosyanın başına bir içerik eklemiş olduk
#     file.seek(0) #dosyaya dahil ettik
#     file.write(content)
# with open("newfile","r",encoding='utf-8') as file:
#     print(file.read())



#******sayfanın ortasına bilgi ekleme ve güncelleme
# with open("newfile","r+",encoding='utf-8') as file:
#    list = file.readlines()
#    list.insert(1,"ali korkmaz\n") #1. indekse ali korkmazı yazdırdık devamı değişmeden yazdırılır 1. indeksteki 2. indekse kaymış olur
#    file.seek(0)#dosyaya dahil ettik
#    for i in list:
#        file.write(i) #her bir liste elemanını tek tek yazdırdık

# with open("newfile","r",encoding='utf-8') as file:
#     print(file.read())

#**for döngüsü ile yazdırmamak için

with open("newfile","r+",encoding='utf-8') as file:
   list = file.readlines()
   list.insert(1,"yılmaz aygün\n") #1. indekse ali korkmazı yazdırdık devamı değişmeden yazdırılır 1. indeksteki 2. indekse kaymış olur
   file.seek(0)#dosyaya dahil ettik
   file.writelines(list)

with open("newfile","r",encoding='utf-8') as file:
    print(file.read())

