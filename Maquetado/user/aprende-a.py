import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AprendeA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprende a...")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("B.TButton", font=('Verdana', 12), foreground="black", background="white", borderwidth=1, padding=10)
        self.style.map('B.TButton', background=[('active', '#1E88E5')], foreground=[('active', 'white')])
        self.style.configure("TFrame", background="white")

        # Frame contenedor (Pone fondo en blanco)
        self.fr = ttk.Frame(self, style="TFrame")
        self.fr.pack()

        # Boton: Volver al inicio
        self.label = ttk.Button(self.fr, text="Volver al inicio", style="B.TButton", command=self.prueba)
        self.label.grid(row=0,column=1, sticky="w", padx=10, pady=10)

        # Boton: a la izquierda
        self.imagenBTNIZQ = Image.open("BTNIZQ.png")
        self.ObjImgBtnIzq = ImageTk.PhotoImage(self.imagenBTNIZQ)
        self.BtnIzq = tk.Button(self.fr, image=self.ObjImgBtnIzq, borderwidth=0, bg="white", command=self.prueba)
        self.BtnIzq.grid(row=2,column=0, sticky="w", padx=10, pady=10)

        # Label: contenedor de imagen
        self.imagenContenedor= Image.open("Contenedor.png")
        self.ObjImgContenedor = ImageTk.PhotoImage(self.imagenContenedor)
        self.Contenedor = tk.Label(self.fr, image=self.ObjImgContenedor)
        self.Contenedor.grid(row=1,column=1, sticky="nsew", rowspan=3, padx=10, pady=10)

        # Boton a la derecha
        self.imagenBTNDER = Image.open("BTNDER.png")
        self.ObjImgBtnDer = ImageTk.PhotoImage(self.imagenBTNDER)
        self.BtnDer = tk.Button(self.fr, image=self.ObjImgBtnDer, borderwidth=0, bg="white", command=self.prueba)
        self.BtnDer.grid(row=2,column=2, sticky="w", padx=10, pady=10)

    def prueba(self):
        print("Opcion presionada")

if __name__ == "__main__":
    root = AprendeA()
    root.mainloop()