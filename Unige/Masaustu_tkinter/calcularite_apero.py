
import tkinter as tk 
PRIX_SODA = 1.20
PRIX_CHIPS = 0.80

root = tk.Tk() 

nb_pers = tk.IntVar(value=0)
prix = tk.StringVar(value="0 chf")

def calculer_prix():
    prix_valuer = nb_pers.get()*PRIX_SODA + nb_pers.get()*PRIX_CHIPS
    prix.set(f'{prix_valuer} CHF')

entree_nb_pers = tk.Entry(root, textvariable=nb_pers)
calculer_apero = tk.Button(root, text="Calculer l'apero ", command=calculer_prix)
affiche_prix = tk.Label(root, textvariable=prix)

entree_nb_pers.grid(row=0 )
calculer_apero.grid()
affiche_prix.grid()

root.mainloop()


