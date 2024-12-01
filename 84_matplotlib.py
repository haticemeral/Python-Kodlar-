import matplotlib.pyplot as plt
import numpy as np

# ÖRNEK1
# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x,y,"o--r")# o yuvarlak işaretli(marker); -- kesikli çizgi şeklinde(stil); r yani red kırmızı(color)
# plt.axis ([0,6,0,20]) #x için 0 6 arası; y için 0-20 arası alındı

# plt.title("grafik başlığı")
# plt.xlabel("x label")
# plt.ylabel("ylabel")
# plt.show()

# ÖRNEK2
# x = np.linspace(0,2,100)
# plt.plot(x,x,label="lineer",color="red")
# plt.plot(x,x**2,label="quadratic",color="yellow")
# plt.plot(x,x**3,label="cubic",color="green")

# plt.xlabel("simple plot")
# plt.ylabel("y label")

# plt.title("simple plot")
# plt.legend()#hangi rengin neye karşılık geldiğini köşede gösterir
# plt.show()


# ÖRNEK3 alt alta birden fazla grafik koyma

# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2)# 2 tane tablo oluşturur

# axs[0].plot(x,x,color="red")
# axs[0].set_title("linear")
# axs[1].plot(x,x**2,color="green")
# axs[1].set_title("quadratic")

# plt.tight_layout()#başlıklar karışmasın diye
# plt.show()

# ÖRNEK4
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2) # 2*2lik toplam 4 tane tablo oluşturur
axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")

plt.show()