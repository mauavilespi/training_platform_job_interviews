import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VerReporte(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inside Out")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("BW.TLabel", font=('Verdana', 18), foreground="black", background="white", padding=10)
        self.style.configure("TButton", foreground="white", font=('Verdana', 14), background="#1E88E5", borderwidth=1, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('TButton', background=[('active', '#1E88E5')])
        self.style.configure("TFrame", background="white")

        # Frame contenedor (Pone fondo en blanco)
        self.fr = ttk.Frame(self, style="TFrame")
        self.fr.pack()

if __name__ == "__main__":
    root = VerReporte()
    root.mainloop()