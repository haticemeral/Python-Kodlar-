# BANKAMATİK UYGULAMASI

SadikHesap = {
    'ad':'sadık turan',
    'hesapNo':'125324652',
    'bakiye':3000,
    'ekhesap':2000
}
AliHesap = {
    'ad':'ali turan',
    'hesapNo':'123324652',
    'bakiye':2000,
    'ekhesap':1000
}
def paraCek(hesap, miktar):
    print(f"merhaba {hesap['ad']}")
    if(hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilrisiniz')
        bakiyeSorgula(SadikHesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']
        if (toplam>=miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı(e/h)')
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekhesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgula(SadikHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(SadikHesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır ek hesap limitiniz ise {hesap['ekhesap']} tl")

paraCek(SadikHesap,3000)
print("*******************")
paraCek(SadikHesap,2000)
print("*******************")
paraCek(AliHesap,5000)