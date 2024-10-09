# # meteo = input("Quelle est la meteo (BEAU = 0 or FROID = 1 or PLEUT = 2)")

# if meteo == 2:
#     print("Hava yap")
# elif meteo == 1:
#     print("Hava yap")
# else:
#      print("Hava yap")

# for i in range(10):
#     pass

# i=0
# while i<9:
#     i= i+1
#     pass #print(i)

import numpy as np
nombre_lancer = int(input("Nombres de lancers"))
somme = 0

for _ in range(nombre_lancer):
    valeur_de = np.random.randint(1,7)
    somme = somme + valeur_de

print("moyenne ="+str(somme/nombre_lancer))
