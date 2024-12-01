html_doc=""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title> <!--web sitesi adı-->
</head>
<body>
    <h1 id="header"> <!--büyük başlık-->
        python kursu
    </h1>
    <div class="grup1">
        <h2> <!--daha küçük başlık-->
            programlama
        </h2>

        <ul> <!--sıralı liste-->
            <li>menü 1 </li> <!--liste elemanları-->
            <li>menü 2 </li>
            <li>menü 3 </li>

        </ul>
    </div>

    <div class="grup2">
        <h2> <!--daha küçük başlık-->
            modüller
        </h2>

        <ul> <!--sıralı liste-->
            <li>menü 1 </li> <!--liste elemanları-->
            <li>menü 2 </li>
            <li>menü 3 </li>

        </ul>
    </div>


    <div class="grup3">
        <h2> <!--daha küçük başlık-->
            django
        </h2>

        <ul> <!--sıralı liste-->
            <li>menü 1 </li> <!--liste elemanları-->
            <li>menü 2 </li>
            <li>menü 3 </li>

        </ul>
    </div>


    <!--resim ekleme    <img src="resminadı" alt="">  -->
    <a class="sister" href="http://example1.com/elsie" id_"lin1>Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id_"lin1>Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id_"lin1>Elsie</a>


</body>
</html>
"""
#uzun bir metin olduğu için 3 çift tırnak kullandık

from bs4 import BeautifulSoup #import ettik

soup = BeautifulSoup(html_doc, "html.parser") 
result = soup.prettify() #html etiketlerini düzenler konsola düzeltilmiş şekilde gelir
result = soup.title #html etiketleri içinden title bilgileri gelir
result = soup.head #html kodları arasından head kısmı gelir
result = soup.body #html kodları arasından body kısmı gelir


result = soup.title.name #title etiketinin adı gelir yani çıktısı title olur
result = soup.title.string #title etiketleri arasındaki string gelir

result = soup.h1 #h1 etiketi ve içeriği gelir
result = soup.h1.string #h1 etiketinin içindeki string gelir
result = soup.h2 #satfadaki ilk h2 etiketi içeriği ile birlikte gelir
result = soup.h2.name #sadece h2 etiketinin adı gelir
result = soup.h2.string #h2 etiketinin içindeki string gelir

result = soup.find_all('h2') #tüm h2 etiketlerini içeriği ile liste şeklinde getirir 

result = soup.div #sayfadaki ilk div i getirir
result = soup.find_all('div')#tüm divleri getirir
result = soup.find_all('div')[1] #1. indisteki divi yani 2. divi getirir(indisler 0dan başlar)
result = soup.find_all('div')[1].ul #2. divin altındaki ul etiketi ve içeriği getirilir
result = soup.find_all('div')[1].ul.li#2. div içindeki ilk li yi içeriğiyle beraber getirir
result = soup.find_all('div')[1].ul.find_all('li') #2. div içindeki tüm li leri içeriğiyle beraber getirir

result = soup.div.findChildren() #ilk divin altındaki tüm alt elemanları getirir

result = soup.div.findNextSibling() #bir sonraki kardeş divi getirir (bir üst satırda 1. div getirilmişti bu satır 2. divi getirir)

result = soup.div.findNextSibling().findNextSiblings()  #bir sonraki kardeş divi getirir (iki kez ard arda yazıldığı için 3. divi getirir)
result = soup.div.findNextSibling().findNextSiblings().findPreviousSibling() #iki kez bir sonraki divi getirirdikten sonra çıktı olarak bir önceki divi getirir(1. div sonra 2. divi sonra 3. divi getirir ve bir önceki div olan 2. dive dönüp onu getirir)

result = soup.find_all('a')#tüm a etiketleri gelir
for link in result:#tüm a linkleri üzerinde dolaşalım
    print(link)

for link in result:
    print(link.get('href')) #istediğimiz özelliğe get metodu ile ulaşabiliriz

print(result)
