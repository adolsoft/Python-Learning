
import tkinter as tk 

root = tk.Tk()

entry = tk.Entry(root, foreground='blue')
entry.grid()

btn = tk.Button(root, text="Merhaba ", cursor="pirate")
btn.grid()
root.mainloop()