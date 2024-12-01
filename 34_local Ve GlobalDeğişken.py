#Fonksiyonlar tanımlandığında kendi içlerinde yeni bir tanımlama alanı (scope) oluştururlar dolayısıyla fonksiyon içinde ya da dışında tanımlanan değişkenlerin nasıl ele alındığını öğrenmemiz gerekir.

#Local ve Global Scope
#Her fonksiyon tanımlandığında kendi tanımlama alanlarını oluştururlar ve kendi içlerinde tanımlanan değişkenler local yani yerel değişken olarak adlandırılırlar.
#Örnek
# global scope
x = 'global x'

def function(): 
    # local scope
    # x = 'local x'
    print(x)

function() # local x
print(x)   # global x  

#Aynı isimde tanımlanan x değişkeni hem global hem de local olarak tanımlanmıştır. Dolayısıyla fonksiyon içerisinde x değişkenine yapılan atama global alanda tanımlanan değişkeni etkilemez çünkü fonksiyon kapsamında yeni bir scope tanımlanır.
#Peki fonksiyon kapsamın x değişkenini tanımlamazsak ne olur ?
#Örnek
# global scope
x = 'global x'

def function(): 
    # local scope    
    print(x)

function() # global x
print(x)   # global x  
#Bu durumda fonksiyon kapsamında x' e ulaşılmaya çalışıldığında kendi kapsamın x olmadığından global kapsamdaki x değeri kullanılır.
#Örnek
# global
name = 'Çınar'

def changeName(new_name):
    # local 
    name = new_name
    print(name)

changeName('Ada') # Ada
print(name)       # Çınar
#changeName() fonksiyonuna gönderdiğimiz değer fonksiyon kapsamındaki name değişkenine atanacağından dolayı değişiklik global değil yerel name değişkeninde yapılmış olur. Dolayısıyla ekrana Ada ve Çınar bilgisi yazılır.

#Nesned Function Scopes
#Peki iç içe tanımladığımız fonksiyon kapsamlarındaki değişkenler nasıl ele alınıyor?
#Örnek
name = 'global string'

def greeting():
    name = 'Çınar'

    def hello():
        print('hello '+ name)

    hello()

greeting() # hello Çınar
#hello() fonksiyonu kapsamında tanımlanan name değişkeni olmadığından dolayı bir üstteki greeting() fonksiyonu kapsamında bulunan name='Çınar' bilgisi hello kapsamında kullanılır. 

#Eğer ki hello() kapsamına name isminde bir değişken eklersek bu durumda hello() için yerel olan name kullanılır.
#Örnek
name = 'global string'

def greeting():
    name = 'Çınar'

    def hello():
        name = 'Ada'
        print('hello '+ name)

    hello()

greeting() # hello Ada
#Peki hello ve greeting içinde name bilgilerini silersek bu durumda tüm fonksiyonlar için global olan name bilgisi ekrana yazdırılır.
#Örnek
name = 'global string'

def greeting():

    def hello():
        print('hello '+ name)

    hello()

greeting() # global string