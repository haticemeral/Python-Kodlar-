#dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
#kullanım: open(dosya_adı, dosyaya_erişme_modu)
#dosya_erişme_öodu => dosyayı hangi amaçla açtığımızı belirtir

# "w":(write)yazma modu.
# dosyayı konumda oluşturur
# dosya içeriğini siler ve yeniden ekleme yapar
file = open("newfile.txt","w",encoding= 'utf-8') #oluşturuldu encoding= 'utf-8' eklentisi ile türkçe karakter kullnaımı sağlandı
file.write("sadık turan") #dosyaya yazma işlemi yapıldı
file.close()

# "a":(append)ekleme.
# dosyayı konumda yoksa oluşturur
# dosyanın sonuna ekleme yapar
file = open("newfile.txt","a",encoding='utf-8')
file.write("\nçınar turan")


# "x":(create)oluşturma.
# dosya zaten varssa hata verir
file = open("newfile2.txt","x",encoding='utf-8')

# "r":(read)okuma.varsayılan dosya konumda yoksa hata verir
