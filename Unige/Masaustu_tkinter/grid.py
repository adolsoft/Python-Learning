import tkinter as tk

root = tk.Tk()


entry = tk.Entry(root, foreground='blue')
btn1 = tk.Button(root, text="Gauche ")
btn2 = tk.Button(root, text="Droit ")

#btn1.grid()
entry.grid(row=1,column=1)
btn1.grid(row=2,column=1)
btn2.grid(row=2,column=2)

root.mainloop()