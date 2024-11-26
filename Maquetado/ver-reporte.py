import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VerReporte(tk.Tk):
    def __init__(self):
        # Ventana
        super().__init__()
        self.title("Inside Out")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.configure("TLabel", font=('Verdana', 18, "bold"), foreground="#1E88E5", background="white", padding=10, relief="flat")

        self.style.configure("VO.TButton", foreground="white", font=('Verdana', 14), background="#1E88E5", borderwidth=0, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('VO.TButton', background=[('active', '#1E88E5')])
        self.style.configure("EL.TButton", foreground="white", font=('Verdana', 14), background="#E57373", borderwidth=0, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('EL.TButton', background=[('active', '#E57373')])

        self.style.configure("TFrame", background="white")

        self.style.configure("Treeview", foreground="black", background="white", font=('Verdana', 12), padding=10)
        self.style.configure("Treeview.Heading", foreground="black", background="white", font=('Verdana', 15), padding=12)
        self.style.map("Treeview.Heading", background=[('active', 'white')])

        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack(side=tk.TOP, fill=tk.X)

        # Obtener imagenes para las emociones
        self.emo_disgusto = tk.PhotoImage(file="./emociones/disgusto-s.png")
        self.emo_enojo = tk.PhotoImage(file="./emociones/enojo-s.png")
        self.emo_feliz = tk.PhotoImage(file="./emociones/feliz-s.png")
        self.emo_miedo = tk.PhotoImage(file="./emociones/miedo-s.png")
        self.emo_neutral = tk.PhotoImage(file="./emociones/neutral-s.png")
        self.emo_sorpresa = tk.PhotoImage(file="./emociones/sorpresa-s.png")
        self.emo_triste = tk.PhotoImage(file="./emociones/triste-s.png")

        # Titulo del reporte
        self.titulo = ttk.Label(self.contenedor, text="1 de nov - 7:00 am (22 mins)")
        self.titulo.pack(side=tk.TOP, fill=tk.X)

        # Contendor de reporte (Treeview con varias columnas)
        self.tablareporte = ttk.Treeview(self.contenedor, columns=("Disgusto", "Enojo", "Feliz", "Miedo", "Neutro", "Sorpresa", "Triste"))
        # Configurando columnas
        self.tablareporte.column("#0", width=400, anchor=tk.W)
        self.tablareporte.column("Disgusto", width=170, anchor=tk.CENTER, stretch=tk.YES)
        self.tablareporte.column("Enojo", width=140, anchor=tk.CENTER)
        self.tablareporte.column("Feliz", width=125, anchor=tk.CENTER)
        self.tablareporte.column("Miedo", width=130, anchor=tk.CENTER)
        self.tablareporte.column("Neutro", width=145, anchor=tk.CENTER)
        self.tablareporte.column("Sorpresa", width=160, anchor=tk.CENTER)
        self.tablareporte.column("Triste", width=130, anchor=tk.CENTER)
        # Titulo de de columnas
        self.tablareporte.heading("#0", text="Pregunta")
        self.tablareporte.heading("Disgusto", text="Disgusto", image=self.emo_disgusto)
        self.tablareporte.heading("Enojo", text="Enojo", image=self.emo_enojo)
        self.tablareporte.heading("Feliz", text="Feliz", image=self.emo_feliz)
        self.tablareporte.heading("Miedo", text="Miedo", image=self.emo_miedo)
        self.tablareporte.heading("Neutro", text="Neutro", image=self.emo_neutral)
        self.tablareporte.heading("Sorpresa", text="Sorpresa", image=self.emo_sorpresa)
        self.tablareporte.heading("Triste", text="Triste", image=self.emo_triste)
        # Inserta elemento
        self.elemento = self.tablareporte.insert(
            "",
            tk.END,
            text="¿Pregunta 1? 34 seg",
            values=("0%", "0%", "0%", "80%", "5%", "15%", "0%")
        )
        self.elemento = self.tablareporte.insert(
            "",
            tk.END,
            text="¿Pregunta 2? 50 seg",
            values=("0%", "0%", "0%", "80%", "5%", "15%", "0%")
        )
        self.elemento = self.tablareporte.insert(
            "",
            tk.END,
            text="¿Pregunta 3? 40 seg",
            values=("0%", "0%", "0%", "80%", "5%", "15%", "0%")
        )
        self.elemento = self.tablareporte.insert(
            "",
            tk.END,
            text="¿Pregunta 4? 10 seg",
            values=("0%", "0%", "0%", "80%", "5%", "15%", "0%")
        )
        # Obteniendo valor de las columnas de un elemento
        print(self.tablareporte.set(self.elemento))
        # Obteniendo el valor de una columna específica
        print(self.tablareporte.set(self.elemento, "Disgusto"))
        # Estableciendo un nuevo valor (Cambia 5 % pot 10%)
        print(self.tablareporte.set(self.elemento, "Neutro", "10%"))

        # Scroll
        self.scrollY = ttk.Scrollbar(self.contenedor, command=self.tablareporte.yview)
        self.scrollY.pack(side=tk.RIGHT, fill=tk.Y)

        self.tablareporte.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        # Boton: Eliminar
        self.Eliminar=ttk.Button(self, text="Eliminar", command=self.prueba, style="EL.TButton")
        self.Eliminar.pack(side=tk.LEFT, fill=tk.BOTH)
        # Boton: Volver
        self.Volver=ttk.Button(self, text="Volver", command=self.prueba, style="VO.TButton")
        self.Volver.pack(side=tk.LEFT, fill=tk.BOTH)

    def prueba(self):
        print("Opcion presionada")


if __name__ == "__main__":
    root = VerReporte()
    root.mainloop()