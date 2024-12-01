#web sitelerinden gerekli kısımları alma işlemi:web scraping

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content# content fonksiyonu ile geriye dönen değer sayesinde html kodlarını aldık
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit=50)#claası lister list olan tbody etiketini ve içeriğini getirip içindeki tüm tr leri getirir
#find_all("tr", limit=1) ifadesiyle tr lerden sadece birini alabiliriz
count = 1
for tr in list: 
    title = tr.find("td",{"class":"titleColumn"}).find("a").text #film isimlerini aldık ve yazdırdık
    year = tr.find("td",{"class":"titleColumn"}).find("span").text #film yıllarını aldık ve yazdırdık
    #year = tr.find("td",{"class":"titleColumn"}).find("span").text.sprit("()") yazarsak yılların içinde bulundağu parantezleri silmiş oluruz
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text #film ratinglerini aldık ve yazdırdık

    print(f"{count}-film: {title.ljust(50)} yıl: {year} değerlendirme: {rating}")
    count+=1#l.just fonksiyonu ile film isimlerini hizaladık


