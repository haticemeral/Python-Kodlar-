# herhangi bir mod verilmemişse bile varsayılan olarak r atanmış olur

# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     file.close()




# file = open("newfile.txt","r",encoding='utf-8')
# #for döngüsü
# for i in file:
#     print(i, end="") #virgülden aralarda boşluk bırakmaması için yazıldı
# file.close()




#************read() fonksiyonu
# file = open("newfile.txt","r",encoding='utf-8')
# content = file.read() #dosyadaki bilgileri okur
# print(content)
# file.close()



# file = open("newfile.txt","r",encoding='utf-8')
# content1 = file.read() 
# print("içerik 1")
# print(content1)

# content2 = file.read()
# #içerik2 deb önce dosya açma işlemini yapsaydık dosyayı en başından okurdu
# print("içerik2") #içeirk2 den önce dosyada okuyacak bir bilgi kalmamıştır imleç en sondadır bu yüzden içerik2 den sonra okunacak bir bilgi yok
# print(content2)
# file.close()


#parametreli okuma
"""
file = open("newfile.txt","r",encoding='utf-8')
content = file.read(5) #ilk 5 karakteri okur
content = file.read(3) #5 karakterden sonraki 3 karakteri okur(boşlukları da karakterden sayar)
print = content
file.close()
"""


#************readline() fonksiyonu
#her defasında bir satır okur
# file = open("newfile.txt","r",encoding='utf-8')
# print(file.readline(),end="") #ilk satırı okur
# print(file.readline(),end="") #kaladığı satırı okur
# print(file.readline(),end="") #kaladığı satırı okur
# #satır bittikten sonra readline çalıştırılırsa bir satırlık boşluk ekler
# file.close()



#************readlines() fonksiyonu
# file = open("newfile.txt","r",encoding='utf-8')
# liste = file.readlines() #dosyadaki her satır bilgiyi listenin bir elemanı olacak şekilde ayarlayıp liste yapar
# print(liste)
# file.close()



