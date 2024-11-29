import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Inicio(tk.Tk):
    def __init__(self):
        # Ventana principal
        super().__init__()
        self.title("Inside Out")
        self.config(bg="white")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("BW.TLabel", font=('Verdana bold', 18), foreground="black", background="white", padding=10)
        self.style.configure("TButton", foreground="white", font=('Verdana', 14), background="#1E88E5", borderwidth=1, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('TButton', background=[('active', '#1E88E5')])
        self.style.configure("TFrame", background="white")

        # Frame
        self.fr = ttk.Frame(self, style="TFrame")
        self.fr.pack()

        # Label: Bienvenidos
        self.label = ttk.Label(self.fr, text="¡Bienvenido!", style="BW.TLabel")
        self.label.grid(row=0,column=0, sticky="w", padx=10, pady=10)

        # Botónes: Lista de opciones
        self.aprendeCV = ttk.Button(self.fr, text="Aprende a redactar tu CV", style="TButton", command=self.abrir_aprende_a_CV)
        self.aprendeCV.grid(row=1,column=0, sticky="w", padx=10, pady=10)

        self.aprendeEntrevista = ttk.Button(self.fr, text="Aprende a preparar tu entrevista", style="TButton", command=self.abrir_aprende_a_Entrevista)
        self.aprendeEntrevista.grid(row=2,column=0, sticky="w", padx=10, pady=10)

        self.practica = ttk.Button(self.fr, text="Practica tu entrevista", style="TButton", command=self.abrir_configura_practica)
        self.practica.grid(row=3,column=0, sticky="w", padx=10, pady=10)

        self.historial = ttk.Button(self.fr, text="Historial", style="TButton", command=self.abrir_historial)
        self.historial.grid(row=4,column=0, sticky="w", padx=10, pady=10)

        # Label: Imagen de abajo
        self.imagen = Image.open("happy.png")
        self.HappyFace = ImageTk.PhotoImage(self.imagen)
        self.labelIMG = tk.Label(self.fr, image=self.HappyFace, borderwidth = 0)
        self.labelIMG.grid(row=3, column=1, rowspan=2, sticky="se", padx=10, pady=10)

    def abrir_aprende_a_CV(self):
        print("Aprende a")

    def abrir_aprende_a_Entrevista(self):
        print("Aprende a")

    def abrir_configura_practica(self):
        print("Configura practica")

    def abrir_historial(self):
        print("Historial")

if __name__ == "__main__":
    root = Inicio()
    root.mainloop()