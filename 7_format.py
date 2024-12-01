# format
name = 'çınar'
surname = 'turan'
print('my name is {} {}'.format(name, surname))
print('my name is {0} {1}'.format(name, surname))
print('my name is {1} {0}'.format(name, surname))
print('my name is {n} {s}'.format(n=name, s=surname))
print('my name is {s} {n}'.format(n=name, s=surname))
age = 36
print('my name is {} {} and i am {} years old'.format(name, surname, '36'))
print('my name is {} {} and i am {} years old'.format(name, surname,age))

result = 200/700
print('the result is {}'.format(result))

print('the result is {r:1.3}'.format(r=result)) # r:1.3 demek tam kısımın önündeki genişiliği belirler kaç karakter olacağını gösterir, ondalıklı kısımdan 3 basamak göster demek

# fstring
print(f"my name is {name} {surname} and i am {age} years old")

