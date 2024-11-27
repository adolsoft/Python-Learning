import tkinter as tk

def get_tasks():
    # Récupération des tâches depuis le fichier tasks.txt
    with open("tasks.txt","r", encoding="utf-8") as f:
        raw_tasks = f.readlines()
        tasks = []
        for t in raw_tasks:
            infos = t.split(",")
            tasks.append((infos[0],tk.IntVar(value=int(infos[1]))))
        return tasks

def save_tasks(tasks):
    # Sauvegarde des tâches dans le fichier tasks.txt
    with open("tasks.txt","w", encoding="utf-8") as f:
        for t in tasks:
            f.write(f"{t[0]},{t[1].get()}\n")