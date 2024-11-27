import tkinter as tk

form = tk.Tk()
form.geometry('500x500+350+250') # konumlandırıldı
form.title('Ders 4')

form.state('normal')
#form.state('zoomed') # çalıştığı zaman tam ekran olarak gelir.
#form.state('iconic') # iconik olarak gelir

# pencereyi saydamlaşma
#form.wm_attributes('-alpha',0.3) # 1 yazarsan norlma gösterilirç
form.wm_attributes('-alpha',0.5)

label1=tk.Label(form, text='Python Tkinter')
label1.pack()

form.mainloop()