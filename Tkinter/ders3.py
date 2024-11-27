import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri-3")
form.geometry('500x250+500+350')
#form.minsize(450,400)
#form.maxsize(550,500)

form.resizable(False,False) #n ekra üzerinde büyütme veye kücütme olmaz.


label=tk.Label(form, text='Ders 3 ')
label.pack()


form.mainloop()