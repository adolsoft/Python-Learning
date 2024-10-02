vitesse = 50
temps_secondes = 2 * 60 * 60

distance = vitesse * ( temps_secondes / 3600 )

print(distance)

#Verifier si le nombre de kilometres parcous est pair impair

est_pair = (distance % 2) == 0
print(est_pair)

#Hızı ve seyahat süresini açıklayan bir cümle oluşturun /  Cree une phrase devrivant la vitesse et le temps de trajet

phrase = "La vitesse est de " + str(vitesse) + " km/h et le temps " + str(temps_secondes) +" second."
print(phrase)

vitesse_legale = 120

est_legale = vitesse < vitesse_legale

pr