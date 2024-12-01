import re

#re modülü
str = "python kursu: python programlama 40 saat"

#re.findall()
# result = re.findall("python",str) #str içinde gönderilen ilk parametreyi arar ve liste şeklinde geri dönderir
# result = len(result)#kaç tane olduğunu bulmak için

# #re.split()
# result = re.split(' ',str)#verilen ilk parametreye göre istenen karakteri(boşlukları) bularak str yi liste şeklinde geri dönderir

# #re.sub()
# result = re.sub(' ','-',str)#son parametredeki str içinden ilk parametrede verilen karakterleri bulur ve yerine ikinci parametredeki karakteri koyup dönderir
# #boşluk yerine \s yazabilirdik

#re.search()
# result = re.search("python",str)#str içinden ilk parametreyi bulur ve indeksiyle beraber dönderir
# result = result.span()#sadece konumunu dönderir
# result = result.start()#kaçıncı indeksten başladığını dönderir
# result = result.end()#kaçıncı indekste bittiğini dönderir
# result = result.group()#bulduğu ifaedeyi gönderir
# result = result.string()#nere içinde arama yaptığımızı değeri ile gösterir(str nin içindekileri yazar)


#regular expression
"""
[]- köşeli parantezler arasına yazılan bütün karakterler aranır
        [abc]=> a: 1 match
                ac: 2 match
                python: no matches

        [a-e]=>[abcde]
        [1-5]=>[12345]
        [0-39]=>[01239] # 0 3 arası bakar ekstra 9 u arar
        #mesala [0-395] 0 ile 3 arası arar ekstra 9 ve 5i arar

        [^abc]=> abc dışındaki karakterler
        [^0-9]=>rakam olmayan karakterler


"""
result = re.findall("[abc]",str) #a b c yi arar
result = re.findall("[pyt]",str) #p y t yi arar
result = re.findall("[a-e]",str) #a e arası tüm karakterleri arar


"""
        . -herhangi bir tek karakteri belirtir
        .. =>   a:no match
                ab:1 match
                abc:1 match
                abcd:2 matches
"""
result = re.findall("...",str)#her 3lü grubu liste şeklinde döndürür
result = re.findall("py..on",str)#başı py sonu on olanları getirir.ortadaki noktaya denk gelen kısımlar fark etmez



"""
        ^ - belirtilen karakterle başlıyor mu
        ^a => a:1 match
            abc:1 match
            bac:no match

"""
result = re.findall("^p",str)# p ile başlayan ifade var mı(str nini p ile başlayıp başlamadığını kontrol eder)


"""     
        $ -belirtilen karakter ile bitiyor mu
        a$ => a:1 match
             lamba:1 match
             python:no matches

"""
result = re.findall('t$',str)#str nin t ile bitip bitmedğinin kontrol eder
result = re.findall('a$',str)#str nin a ,le bitip bitmediğini kontrol eder
result = re.findall('programlama$',str) #str nin programlama ile bitip bitmediğini kontrol eder

"""
        * -bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder
                        ma*n => mn: 1 match
                                man: 1 match
                                maan: 1 match
                                maaan: 1 match
                                main: no match(a'nın arkasından n gelmiyor)

"""
result = re.findall("sa*t",str)


"""
        + -bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder
        ma+n => mn: no match
                man: 1 match
                maan: 1 match
                main: no match(a'nın arkasından n gelmiyor)

"""
result = re.findall("saa+t",str)#a karakterinden en az bir tane olacak

"""
        ? -bir karakterin sıfır ya da bir kez olmasını kontrol eder
        ma?n => mn: no match
                man: 1 match
                maan: 1 match
                main: no match(a'nın arkasından n gelmiyor)

"""
result = re.findall("sa?t",str)


"""
        {} - karakter sayısını kontrol eder
                al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlanmalı
                al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlanmalı
                [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar
"""
result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)

"""
        | -alternatif seçeneklerden birinin gerçekleşmesi gerekir
                a|b => a ya da b
                cde: no match
                ade: 1 match
                acdbea: 3 match

"""

"""
        () - gruplamak için kullanılır
                (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir
"""


"""
        \ -özel karakterleri aramamızı sağlar
                \$a => $ karakterinin arkasına a karakterini arar yani $ regular exp. engine tarafından yorumlanmaz

                
        \A -belirtilen karakter stringin başında mı
                \Athe => the string in başında mı

        \Z -belirtilen karakter stringin sonunda mı
                the\Z => the stringin sonunda mı

        \b -belirtilen karakter stringin başında ya da sonunda mı
                \bthe =>the string in başında mı
                the\b => the stringin sonunda mı

        \B -belirtilen karakter stringin başında ya da sonunda deeğil mi
                \Bthe =>the string in başında değil mi
                the\B => the stringin sonunda değil mi  


        \d -[0-9] ile aynı anlama glir yani rakamları arar
                \d => 12abc34

        \D -[^0-9] ile aynı anlama glir yani rakam olmayanları arar
                \D => 12abc34_50
        
        \s (küçük s)-boşluk karakterlerini arar
        \S (büyük S)-boşluk karkateri dışındakileri arar
        \w (küçük w)-alfabetik karakterler rakamlar ve alt çizgi karkaterlerinin arar
        \W (büyük W)- \w nin tam tersi


"""


print(result)
