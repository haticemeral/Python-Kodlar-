import numpy as np #numpy a np adını vererek import ettik

#python list
py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#numpy küyüphanesi sayesinde normal listeler de yapamadığımız şeyleri yapabiliriz
#hem daha hızlı çalışır hem de daha az yer kaplar

#numpy array
#? TEK BOYUTLU DİZİ
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(py_list))
print(type(np_array))

#? ÇOK BOYUTLU DİZİ
py_multi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #.ok boyutlu liste
print(py_multi)
np_multi = np.reshape(3,3)#diziyi şekilllendirme metodu(3 e 3lük bir çok boyutlu dizi)matris
print(np_multi)

#dizinin boyut sayısını veren fonksiyon
print(np_array.ndim)
print(np_multi.ndim)
