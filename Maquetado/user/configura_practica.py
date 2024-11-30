import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ConfiguraPractica(tk.Toplevel):

    # Atributo de la clase que indica si la ventana secundaria está en uso.
    en_uso = False

    def __init__(self):
        # Ventana
        super().__init__()
        self.title("Configura tu entrevista")

        #  -------------- Estilos -------------- #
        self.style = ttk.Style()
        self.style.theme_use('alt')

        # Titulo blanco y negro
        self.style.configure(
            "BW.TLabel",
            font=('Verdana', 12),
            foreground="black",
            background="white",
            padding=10
        )

        # Boton de confirmar azul
        self.style.configure(
            "CO.TButton",
            foreground="white",
            font=('Verdana', 14),
            background="#1E88E5",
            borderwidth=0,
            focusthickness=3,
            focuscolor='none',
            padding=10
        )
        self.style.map('CO.TButton', background=[('active', '#1E88E5')])

        # Boton de cancelar rojo
        self.style.configure(
            "CA.TButton",
            foreground="white",
            font=('Verdana', 14),
            background="#E57373",
            borderwidth=0,
            focusthickness=3,
            focuscolor='none',
            padding=10
        )
        self.style.map('CA.TButton', background=[('active', '#E57373')])

        # Boton
        self.style.configure(
            "UD.TButton",
            foreground="#1E88E5",
            background="white",
            borderwidth=1
        )
        self.style.map("UD.TButton", background=[('active', '#1E88E5')], foreground=[('active', 'white')])

        # Contenedor con fondo blanco
        self.style.configure("TFrame", background="white")

        # -------------- Componentes -------------- #
        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack()

        # Combobox: Selecciona una categoria
        self.Categorias = ttk.Combobox(
            self.contenedor,
            values=("Selecciona una categoria","Frontend", "Backend", "Softskills"),
            font="Verdana 16 bold"
        )
        self.Categorias.current(0)
        self.Categorias.grid(row=0, column=0, sticky="nsew", columnspan=2, padx=20, pady=10)

        # Label: Numero de preguntas
        self.Etiqueta = ttk.Label(
            self.contenedor,
            text="Número de preguntas:",
            style="BW.TLabel"
        )
        self.Etiqueta.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        #Spinbox: Seleccionar número de preguntas
        self.NumeroPreguntas = ttk.Spinbox(
            self.contenedor,
            from_=1,
            to=30,
            state="readonly",
            font="Verdana 12"
        )
        self.NumeroPreguntas.grid(row=2, column=1, sticky="e", padx=10, pady=10)


        # Label: Duración estimada
        self.EtiquetaDuracion = ttk.Label(
            self.contenedor,
            text="Duración estimada:",
            style="BW.TLabel"
        )
        self.EtiquetaDuracion.grid(row=3,column=0, sticky="e", padx=10, pady=10)
        # Label: Duracion
        self.Duracion = ttk.Label(
            self.contenedor,
            text="01:00",
            style="BW.TLabel"
        )
        self.Duracion.grid(row=3, column=1, sticky="w", pady=10)

        # Boton: Cancelar
        self.Cancelar=ttk.Button(
            self.contenedor,
            text="Cancelar",
            command=self.goback,
            style="CA.TButton"
        )
        self.Cancelar.grid(row=4, column=0, sticky="nsew", pady=10, padx=10)
        # Boton: Confirmar
        self.Confirmar=ttk.Button(
            self.contenedor,
            text="Confirmar",
            command=self.prueba,
            style="CO.TButton"
        )
        self.Confirmar.grid(row=4, column=1, sticky="nsew", pady=10, padx=10)

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
    root = ConfiguraPractica()
    root.mainloop()