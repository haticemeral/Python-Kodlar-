import pandas as pd

customers = {
    'customerId':[1,2,3,4],
    'firstName':['ahmet','ali','hasan','canan'],
    'lastName':['yılmaz','korkmaz','çelik','toprak']
}

orders = {
    'orderId':[10,11,12,13],
    'customerId':[1,2,5,7],
    'orderDate':['2010-07-04','2020-08-04','2010-07-07','2012-07-04']
}

#!tabloları birleştirme
df_customers = pd.DataFrame(customers, columns=["customerId","firstName","lastName"])
df_orders = pd.DataFrame(orders, columns=["orderId","customerId","orderDate"])

#önce tabloları ayrı ayrı yazdıralım
print(df_customers)
print(df_orders)

#şimdi kolonları birleştirelim
result = pd.merge(df_customers,df_orders,how="inner")#birleştirilmiş kolon gelir sadece ortak olanlar
result = pd.merge(df_customers,df_orders,how="left")#birleştirilmiş kolon gelir sadece solda yazan tablodaki değerler gelir orderno su olmayan bilgilerde NaN ile belritilir




print(result)


