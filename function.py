# # 1 
# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Merhaba\n', 10) 

# def listeyecevir(*params): # * dememeiz önemli sınırsı  sayıda arguman alır
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyecevir(10, 20, 30, 'Merhaba')
# print(result)



def asalsayibul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2):
        if sayi > 1 :
            for i in range(2, sayi):
                if (sayi % 2 == 0):
                    break
            else:
                print(sayi)    

sayi1 = int(input("sayi 1 :"))
sayi2 = int(input("sayi 2 :"))

asalsayibul(sayi1, sayi2)