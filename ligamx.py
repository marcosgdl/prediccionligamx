import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

class SorteoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Predicción Liga MX")
        self.geometry("400x500")

        self.configure(bg="#0074D9")  
        self.equipos = [
            "America", "Atlas", "Chivas", "Cruz Azul", "Toluca", "Queretaro",
            "Rayados", "Tigres", "San Luis", "Mazatlan", "Juarez", "Necaxa",
            "Santos", "Leon", "Pachuca", "Pumas", "Puebla", "Xolos"
        ]

        self.image_url = "https://s3.amazonaws.com/lmxwebsite/images/logos_footer/liga_mx_footer.png"
        self.image = self.cargar_imagen(self.image_url)

        self.image_label = tk.Label(self, image=self.image, bg="#0074D9")
        self.image_label.pack(pady=10)

        self.sortear_button = ttk.Button(self, text="Predecir tabla general", command=self.sortear_equipos)
        self.sortear_button.pack(pady=10)

        self.resultados_text = tk.Text(self, height=20, width=40, bg="#999", fg="white")
        self.resultados_text.pack(pady=10)
        self.resultados_text.config(state=tk.DISABLED)

    def cargar_imagen(self, url):
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img.thumbnail((300, 300))
        return ImageTk.PhotoImage(img)

    def sortear_equipos(self):
        equipos_aleatorios = random.sample(self.equipos, len(self.equipos))
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)

        self.resultados_text.tag_configure("verde", foreground="green")
        self.resultados_text.tag_configure("amarillo", foreground="yellow")
        self.resultados_text.tag_configure("rojo", foreground="red")

        for i, nombre in enumerate(equipos_aleatorios, start=1):
            if i <= 6:
                tag = "verde"
            elif 6 < i <= 10:
                tag = "amarillo"
            else:
                tag = "rojo"
            self.resultados_text.insert(tk.END, nombre + "\n", tag)

        self.resultados_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = SorteoApp()
    app.mainloop()

