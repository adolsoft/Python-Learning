# def square(num): return num ** 2
# # bu sayıların her birinin karaesini alalım
# numbers = [1, 2, 5, 9] 
# # dizilerde map metodu ile dizi elemanlarını herbirine ulaşabiliriz.
# ## önemli not map içinde foksiyona gönderme yapabiliriz 
# # ama foksiyonu () işaretlerini yazmadan ekliyoruz. 
# result = list(map(square, numbers))
# # result içine altmamız ya bir list metodu ile yada  for ile içersine göndermemiz gerekiyor
# print(result)
 

#def square(num): return num ** 2

numbers = [1, 2, 5, 9] 

result = list(map(lambda num: num **2 , numbers))

print(result)

# yada
square = lambda num: num **2
numbers = [1, 2, 5, 9] 

result = list(map(square , numbers))

print(result)
 