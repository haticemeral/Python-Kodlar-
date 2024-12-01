#file.close() kulanmamak için
with open("newfile.txt","r",encoding='utf-8') as file: #open ile başlayan uzun kodu file kelimesiyle referans vermiş olduk
    content = file.read(10)#sadece 10 karakter okur
    print(content)
    file.seek(5)#imleci 5. karaktere götürür(karakterler sıfırdan başlayıp numaralandırılır)
    print(file.tell())#tell() fonksiyonu imlecin o andaki konumunu bulabilmek için kullanılır (5. karakterden sonrasını okur bir üst satır yüzünden)
    #imlecin son durumundan sonra okuma yapılmak istenilirse ekrana boş satır gelir