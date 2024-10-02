name = 'Sadık'
surname = 'Turan'
age = 36

greeting = 'My name is ' + name + ' '+ surname + ' and \nI am ' + str(age) + ' years old.'
length = len(greeting)
#print(greeting)

"""
print(greeting[0])
print(greeting[2])
print(len(greeting)) # kaç karekter olduğunu söyler
print(greeting[length-1]) # en son karakter
print(greeting[-1]) # buda en son karakter"
"""
print(greeting[3:7]) # name bilgisi gelir
print(greeting[3:])
print(greeting[:15])
print(greeting[2:40:2]) # 2 den 40 kadar gider birini alır birini almaz