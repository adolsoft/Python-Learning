import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri-1")

label1=tk.Label(form, text='Python Tkinter')
label1.pack()

label2=tk.Label(form, text='Ders 2', fg='red')
label2.pack()

label3=tk.Label(form, text='Ders 2 arkapılan', fg='black', bg='green')
label3.pack()

label4=tk.Label(form, text='yeni label', fg='red', bg='blue', font='Times 15 italic')
label4.pack()

label5=tk.Label(form, text='en Label', fg='green', bg='red', font='Times 17')
label5.pack()

form.mainloop()