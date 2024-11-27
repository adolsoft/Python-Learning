# # Importe le module tkinter et le renomme tk
# import tkinter as tk 

# # Crée la fenêtre principale
# root = tk.Tk() 

# # Ajoute un bouton à la fenêtre
# tk.Button(root, text="Hello World").grid() 

# #principale avec pour texte Hello World
# root.mainloop() # Entre dans la boucle d'évenement pour afficher le contenu et
# #réagir aux interactions

from tkinter import *
from tkinter import ttk
root = Tk()
#ttk.Button(root, text="Hello World").grid()
btn = ttk.Button(root, text="Hello World")
btn.grid()
root.mainloop()