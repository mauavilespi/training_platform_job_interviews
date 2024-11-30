"""
Aprende A
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Sat 30-Nov-2024

Maquetado de los módulos Aprende a crear tu CV y Aprende a preparar tu entrevista
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AprendeA(tk.Toplevel):

    # Atributo de la clase que indica si la ventana secundaria está en uso.
    en_uso = False

    def __init__(self):
        super().__init__()
        self.title("Aprende a...")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')

        # Boton para regresar al inicio
        self.style.configure(
            "GB.TButton",
            font=('Verdana', 14),
            foreground="black",
            background="white",
            borderwidth=1,
            padding=10
        )
        self.style.map('GB.TButton', background=[('active', '#1E88E5')], foreground=[('active', 'white')])

        # Contenedor de fondo blanco
        self.style.configure("TFrame", background="white")

        # Frame contenedor (Pone fondo en blanco)
        self.fr = ttk.Frame(self, style="TFrame")
        self.fr.pack()

        # Boton: Volver al inicio
        self.label = ttk.Button(
            self.fr,
            text="Volver al inicio",
            style="GB.TButton",
            command=self.goback)
        self.label.grid(row=0,column=1, sticky="w", padx=10, pady=10)

        # Boton: a la izquierda
        self.imagenBTNIZQ = Image.open("./assets/BTNIZQ.png")
        self.ObjImgBtnIzq = ImageTk.PhotoImage(self.imagenBTNIZQ)
        self.BtnIzq = tk.Button(self.fr, image=self.ObjImgBtnIzq, borderwidth=0, bg="white", command=self.prueba)
        self.BtnIzq.grid(row=2,column=0, sticky="w", padx=10, pady=10)

        # Label: contenedor de imagen
        self.imagenContenedor= Image.open("./assets/Contenedor.png")
        self.ObjImgContenedor = ImageTk.PhotoImage(self.imagenContenedor)
        self.Contenedor = tk.Label(self.fr, image=self.ObjImgContenedor)
        self.Contenedor.grid(row=1,column=1, sticky="nsew", rowspan=3, padx=10, pady=10)

        # Boton a la derecha
        self.imagenBTNDER = Image.open("./assets/BTNDER.png")
        self.ObjImgBtnDer = ImageTk.PhotoImage(self.imagenBTNDER)
        self.BtnDer = tk.Button(self.fr, image=self.ObjImgBtnDer, borderwidth=0, bg="white", command=self.prueba)
        self.BtnDer.grid(row=2,column=2, sticky="w", padx=10, pady=10)

        # Para que la ventana secundaria obtenga el foco automáticamente una vez creada
        self.focus()
        # El usuario no pueda utilizar la ventana de administrador mientras esta ventana está visible
        self.grab_set()
        # Indicar que la ventana está en uso luego de crearse.
        self.__class__.en_uso = True

    def prueba(self):
        print("Opcion presionada")

    def goback(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()

if __name__ == "__main__":
    root = AprendeA()
    root.mainloop()