"""
Inicio
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Sat 30-Nov-2024

Pantala de inicio que le permitira acceder a los siguientes módulos:
- Aprende a redactar tu CV
- Aprende a prepararte para tu entrevista
- Practica tu entrevistz
- Ver historial de practicas de entrevista
"""

# Importaciones
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Importa ventanas secundarias
from aprende_a import AprendeA
from configura_practica import ConfiguraPractica
from historial import Historial


class Inicio(tk.Tk):
    def __init__(self):
        # Ventana principal
        super().__init__()
        self.title("Inside Out")
        self.config(background="white")

        # -------------- Estilos -------------- #
        self.style = ttk.Style()
        self.style.theme_use('alt')

        # Titulo blanco y negro
        self.style.configure(
            "BW.TLabel",
            font=('Verdana bold', 18),
            foreground="black",
            background="white",
            padding=10
        )

        # Boton azul
        self.style.configure(
            "BL.TButton",
            foreground="white",
            font=('Verdana', 14),
            background="#1E88E5",
            borderwidth=1,
            focusthickness=3,
            focuscolor='none',
            padding=10
        )

        self.style.map('TButton', background=[('active', '#1E88E5')])

        # Contenedor con fondo blanco
        self.style.configure("TFrame", background="white")

        # -------------- Componentes -------------- #
        # Frame contendor
        self.contenedor = ttk.Frame(
            self,
            style="TFrame"
        )
        self.contenedor.pack(padx=50, pady=20)

        # Label: Bienvenidos
        self.label = ttk.Label(
            self.contenedor,
            text="¡Bienvenido!",
            style="BW.TLabel"
        )
        self.label.grid(row=0, column=0, sticky="w", padx=10, pady=10)


        # Botónes: Lista de opciones
        self.aprendeCV = ttk.Button(
            self.contenedor,
            text="Aprende a redactar tu CV",
            style="BL.TButton",
            command=self.abrir_aprende_a_CV
        )
        self.aprendeCV.grid(row=1,column=0, sticky="w", padx=10, pady=10)


        self.aprendeEntrevista = ttk.Button(
            self.contenedor,
            text="Aprende a preparar tu entrevista",
            style="BL.TButton",
            command=self.abrir_aprende_a_Entrevista
        )
        self.aprendeEntrevista.grid(row=2,column=0, sticky="w", padx=10, pady=10)


        self.practica = ttk.Button(
            self.contenedor,
            text="Practica tu entrevista",
            style="BL.TButton",
            command=self.abrir_configura_practica
        )
        self.practica.grid(row=3,column=0, sticky="w", padx=10, pady=10)


        self.historial = ttk.Button(
            self.contenedor,
            text="Historial",
            style="BL.TButton",
            command=self.abrir_historial
        )
        self.historial.grid(row=4,column=0, sticky="w", padx=10, pady=10)


        # Label: Imagen de abajo
        self.imagen = Image.open("./assets/happy.png")
        self.HappyFace = ImageTk.PhotoImage(self.imagen)
        self.labelIMG = tk.Label(
            self.contenedor,
            image=self.HappyFace,
            borderwidth = 0
        )
        self.labelIMG.grid(row=3, column=1, rowspan=2, sticky="se", padx=10, pady=10)


    def abrir_aprende_a_CV(self):
        if not AprendeA.en_uso:
            self.ventana_aprende_CV = AprendeA()

    def abrir_aprende_a_Entrevista(self):
        if not AprendeA.en_uso:
            self.ventana_aprende_entrevista = AprendeA()


    def abrir_configura_practica(self):
        if not ConfiguraPractica.en_uso:
            self.ventana_configura_practica = ConfiguraPractica()


    def abrir_historial(self):
        if not Historial.en_uso:
            self.ventana_historial = Historial()

if __name__ == "__main__":
    root = Inicio()
    root.mainloop()