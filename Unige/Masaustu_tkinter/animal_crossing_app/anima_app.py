import tkinter as tk
from tkinter import font

from PIL import Image, ImageTk

from tasks import get_tasks, save_tasks

# Paramètres globales de l'application
TITLE = "Lecture de plaque d'immatriculation"
TITLE1 = "Lecture de la plaque d'immatriculation du véhicule"
FONT = {
    "family": "Courier",
    "size": 14,
    "weight": "normal"
}
MIN_SIZE = (800,600)


# Gestion de la fenêtre principale utilisée par toutes les pages
root = tk.Tk()
root.title(TITLE)
root.minsize(MIN_SIZE[0],MIN_SIZE[1])

# Gestion des polices globales
basic_font = font.Font(family=FONT["family"],size=FONT["size"],weight=FONT["weight"])
title_font = basic_font.copy()
title_font.configure(size=12,weight="bold")

def home_page():
    DESCRIPTION = """
        Programme qui lit les plaques d'immatriculation des véhicules 
        avec des images téléchargées et conserve les enregistrements 
        de ces véhicules
    """
    # Layout de la fenêtre principale
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

# resim eklemeyi dene
# Görüntüyü yükle 
    image = Image.open("images.jpg") 
    photo = ImageTk.PhotoImage(image)

# Création des widgets et paramètres pour la page d'accueil
    label = tk.Label(root, image=photo) 
    label.image = photo # Görüntünün çöp toplayıcı tarafından kaldırılmasını önler label.grid(row=0, column=0)
    title = tk.Label(root, text=TITLE1,font=title_font)
    description = tk.Label(root, text=DESCRIPTION,font=basic_font)
    continue_btn = tk.Button(root, text="Lancer l'application",font=basic_font,command=continuer)
    




# label.pack()

 # Placement des widgets pour la page d'accueil
    title.grid(row=0,column=1)
    label.grid(row=1,column=0)
    description.grid(row=1,column=1)
    continue_btn.grid(row=2,column=1)

def continuer():
    pass









# Lancement de la boucle principale
home_page()
root.mainloop()