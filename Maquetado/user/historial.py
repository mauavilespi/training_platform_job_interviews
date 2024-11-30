"""
Historial de reportes
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Sat 30-Nov-2024

Aqui el usuario podra ver la lista de reportes que ha podido ir almacenando
puede seleccionar un reporte, esto lo redireccionara a la ventana: Ver Reporte
"""
# Importaciones
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Historial(tk.Toplevel):

    # Atributo de la clase que indica si la ventana secundaria está en uso.
    en_uso = False

    def __init__(self):
        super().__init__()
        self.title("Inside Out")

        #  -------------- Estilos -------------- #
        self.style = ttk.Style()
        self.style.theme_use('alt')

        # Titulo de seccion: "Reportes"
        self.style.configure(
            "TLabel",
            font=('Verdana', 12),
            foreground="#1E88E5",
            background="white",
            padding=10
        )

        # Boton blanco y negro: "Volver al inicio"
        self.style.configure(
            "B.TButton",
            font=('Verdana', 12),
            foreground="black",
            background="white",
            borderwidth=1,
            padding=10
        )
        self.style.map('B.TButton', background=[('active', '#1E88E5')], foreground=[('active', 'white')])

        # Boton azul de confirmación: Abrir reporte
        self.style.configure(
            "A.TButton",
            foreground="white",
            font=('Verdana', 14),
            background="#1E88E5",
            borderwidth=0,
            focusthickness=3,
            focuscolor='none',
            padding=10
        )
        self.style.map('A.TButton', background=[('active', '#1E88E5')])

        # Frame contenedor con fondo blanco
        self.style.configure("TFrame", background="white")

        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack()

        # -------------- Componentes -------------- #
        # Boton: Volver al inicio
        self.volver = ttk.Button(
            self.contenedor,
            text="Volver al inicio",
            style="B.TButton",
            command=self.goback
        )
        self.volver.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Label: Titulo "Reportes guardados"
        self.titulo = ttk.Label(
            self.contenedor,
            text="Reportes guardados",
            style="BW.TLabel"
        )
        self.titulo.grid(row=1, column=0, sticky="w", padx=80, pady=10)

        # Frame: Marco para contener la lista de reportes
        self.contenedorLista = ttk.Frame(self.contenedor)
        # ListBox: Lista de reportes
        self.reportes = tk.Listbox(self.contenedorLista)
        # Crear una barra de deslizamiento con orientación vertical.
        self.scrollbar = ttk.Scrollbar(self.contenedorLista, orient=tk.VERTICAL)
        # Vincularla con la lista.
        self.reportes = tk.Listbox(self.contenedorLista, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.reportes.yview)
        # Ubicarla a la derecha.
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.reportes.pack(fill=tk.X)
        self.contenedorLista.grid(row=2,column=0, sticky="nsew", padx=40, pady=10)

        # Insertar 100 ítems.
        for i in range(1, 101):
            self.reportes.insert(tk.END, f"Elemento {i}")

        # Boton: Abrir
        self.Abrir=ttk.Button(
            self.contenedor,
            text="Abrir",
            command=self.prueba,
            style="A.TButton"
        )
        self.Abrir.grid(row=4, column=0, sticky="nsew", pady=10, padx=10)

        # Para que la ventana secundaria obtenga el foco automáticamente una vez creada
        self.focus()
        # El usuario no pueda utilizar la ventana de administrador mientras esta ventana está visible
        self.grab_set()
        # Indicar que la ventana está en uso luego de crearse.
        self.__class__.en_uso = True


    def goback(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()

    def prueba(self):
        print("Opcion presionada")

if __name__ == "__main__":
    root = Historial()
    root.mainloop()