import tkinter as tk
from tkinter import font

from tasks import get_tasks, save_tasks

# Paramètres globales de l'application
TITLE = "Simple task manager"
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
title_font.configure(size=24,weight="bold")

def home_page():
    DESCRIPTION = """
        Simple task manager à pour but de vous 
        aider à gérer vos tâches quotidiennes.
        Vous pourrez ajouter, supprimer et modifier 
        des tâches en quelques clics.
        Passer un bon moment sur l'application !
    """
    # Layout de la fenêtre principale
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    # Création des widgets et paramètres pour la page d'accueil
    title = tk.Label(root, text=TITLE,font=title_font)
    description = tk.Label(root, text=DESCRIPTION,font=basic_font)
    continue_btn = tk.Button(root, text="Lancer l'application",font=basic_font,command=continuer)

    # Placement des widgets pour la page d'accueil
    title.grid(row=0,column=1)
    description.grid(row=1,column=1)
    continue_btn.grid(row=2,column=1)

def continuer():
    clear_root() # Supprime tout les widgets de la fenêtre 
    to_do_page() # Crée le contenu de la page suivante

def to_do_page():
    DESCRIPTION = """
        Voici la liste de vos 
        tâches à effectuer aujourd'hui.
    """

    # Layout de la fenêtre principale
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)

    # Création des widgets et paramètres pour la page de gestion des tâches
    tk.Label(root, text=DESCRIPTION,font=basic_font).grid(column=0,columnspan=3)

    tasks = get_tasks()
    for task in tasks:
        check_btn = tk.Checkbutton(
            root,text=task[0],font=basic_font,
            variable=task[1]
        )
        check_btn.grid(sticky="w",column=1)
        if task[1].get():
            check_btn.select()
    
    # Gestion de la sauvegarde des tâches lors de la fermeture de l'application
    root.protocol("WM_DELETE_WINDOW", lambda: save_and_quit(tasks))

def save_and_quit(tasks):
    save_tasks(tasks)
    root.destroy()

def clear_root():
    # Suppression de tout les widgets qui sont sur la page principale
    for widget in root.winfo_children():
        widget.destroy()
    for row in range(root.grid_size()[1]):
        root.grid_rowconfigure(row, weight=0)
    for col in range(root.grid_size()[0]):
        root.grid_columnconfigure(col, weight=0)

# Lancement de la boucle principale
home_page()
root.mainloop()