#SELENIUM bir web otomasyon kütüphanesidir
#selenium ile bir web sitesini ziyaret edip etkileşimde bulunabiliriz
from selenium import webdriver
import time
driver = webdriver.Edge()

# url = "http://sadikturan.com"

# driver.get(url)

url = "http://github.com"

driver.get(url)#verilen url adresi ziyaret edilir

time.sleep(2)#2 saniye beklenir
driver.maximize_window()#sayfa büyütülür
driver.save_screenshot("github.com-homepage.png")#verilen adreste bir screenshot alınır ve diğer dosyaların yanına kaydedilir(sol kısımdaki pencerede görünür)

url = "http://github/sadikturan"
driver.get(url)


print(driver.title)#ziyaret edilen sayfanın title bölümünü getirir
time.sleep(2)#2 saniye beklenir

if "sadikturan" in driver.title:#başlık sadıktursn ise ss alınır ve kaydedilir
    driver.save_screenshot("github-sadikturan.png")

driver.back()#sayfayı geri alır(ana sayfaya geri döner)
#driver.forward()#sayfayı ileri alır
time.sleep(2)#2 saniye beklenir
driver.close()#açılan tarayıcı kapatılır