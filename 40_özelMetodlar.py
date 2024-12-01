from typing import Any


mylist = [1, 2, 3]
myString = 'my string'

print(len(mylist))
print(len(myString))

class Movie():
    def __init__(self, title, director, duraction):
        self.title = title
        self.director = director
        self.duraction = duraction
        print('movie objesi oluşturuldu')
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duraction

    def __del__(self):
        print('movie objesi silindi')

   
m = Movie('filmin adı', 'yönetmen adı', 120)
print(type(m))
print(len(m))

print(str(mylist))
print(str(m))

print(len(mylist))
print(len(m))

del m # m objesini sildik
print(m) #hata alırız