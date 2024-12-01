sayi = int(input('say: '))
asalMi = True
if sayi==1:
    asalMi = False
for i in range(2,sayi):
    if(sayi%i==0):
        asalMi = False
        break
if asalMi:
    print('sayı asaldır')
else:
    print('sayı asal değildir.')