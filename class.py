# class

class Person:
    #  class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year): # self yerine başka bir işimde verebiliriz
        pass
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalişti')

        # methods

# object, instance
p1 = Person(name = 'ali', year = 1990) # bu şekildede gönderebiliriz
p2 = Person(name = 'eda', year = 1905)

# updating
p1.name = 'Ahmet'
p1.address = 'Kocaeli'

#accessing object attributes
print(f'p1: name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2: name: {p2.name} year: {p2.year} address: {p2.address}')


print(type(p1))
print(type(p2))

print(p1)
