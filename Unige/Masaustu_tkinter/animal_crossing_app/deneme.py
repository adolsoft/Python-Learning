import tkinter as tk
from PIL import Image, ImageTk

try:
    # Ana pencereyi oluştur
    root = tk.Tk()
    root.title("JPEG Görüntü Göster")

    # Görüntüyü yükle
    image = Image.open("images.jpg")
    photo = ImageTk.PhotoImage(image)

    # Label widget'ında görüntüyü göster
    label = tk.Label(root, image=photo)
    label.image = photo  # Görüntünün çöp toplayıcı tarafından kaldırılmasını önler
    label.grid(row=0, column=0)

    # Diğer widget'lar eklenebilir
    button = tk.Button(root, text="Bir Düğme")
    button.grid(row=1, column=0)

    # Ana döngüyü çalıştır
    root.mainloop()
except Exception as e:
    print(f"Hata: {e}")
