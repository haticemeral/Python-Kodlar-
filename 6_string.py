name = 'sadık'
surname = 'turan'
age = 16

# print("my name is" + name + ' ' + surname + ' and i am ' + age + ' years old.' ) age string olmadığı için hata verir

greeting = 'my name is ' + name + ' ' + surname + ' and i am ' + str(age) + ' years old.' #age değişkeninin tipini değiiştirdik
length = len(greeting)
print(greeting)
print(greeting[0]) #m harfi yazılır
print(greeting[length-1]) #son karakteri yazdırır 
print(greeting[-1]) #son karakteri yazdırır
print(greeting[2:5]) #2. indisten beşinci indise kadar yazdırır  
print(greeting[3:]) #3. indisten başlar sona kadar yazar
print(greeting[:15]) #baştan al ve 15. indise kadar yazdırır
print(greeting[2:40:2]) #2. indisten başla 40. indise kadar git ve ikişerikişer yazar adım sayısı 2dir bir alır bir almaz
print(greeting[3:6])
print(greeting[1:5])
# \n alt satıra geçer