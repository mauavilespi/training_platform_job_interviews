import tkinter as tk
from tkinter import font, ttk, messagebox

class AgregarPregunta(tk.Tk):

    def __init__(self):
        # Ventana principal
        super().__init__()
        self.title("Inside Out")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.configure("C.TEntry", foreground="black", padding=15)

        self.style.configure("GR.TButton", foreground="white", font=('Verdana', 14, 'bold'), background="#66BB6A", borderwidth=0, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('GR.TButton', background=[('active', '#66BB6A')])

        self.style.configure("T.TLabel", font=('Verdana', 12), foreground="black", background="white", padding=10)

        self.style.configure("RE.TButton", foreground="white", font=('Verdana', 14, 'bold'), background="#E57373", borderwidth=0, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('RE.TButton', background=[('active', '#E57373')])

        self.style.configure("TFrame", background="white")

        self.categorias = self.get_categories()

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("TFrame", background="white")

        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack()

        self.ent_pregunta = ttk.Entry(
            self.contenedor,
            width=80,
            font=font.Font(family="Verdana", size=16),
            justify=tk.LEFT,
            style="C.TEntry"
        )
        self.ent_pregunta.grid(row=0, column=0, rowspan=2)

        self.btn_agregar_pregunta = ttk.Button(self.contenedor, text="Agregar", command=self.add_question, style="GR.TButton")
        self.btn_agregar_pregunta.grid(row=0, column=1, padx=10, pady=10)

        self.btn_agregar_pregunta = ttk.Button(self.contenedor, text="Cancelar", command=self.cancel, style="RE.TButton")
        self.btn_agregar_pregunta.grid(row=1, column=1, padx=10, pady=5)

        self.lbl_categorias = ttk.Label(self.contenedor, text="Selecciona la (o las) categoria(s) de la pregunta", style="T.TLabel")
        self.lbl_categorias.grid(row=2, column=0, columnspan=2)

        # Marco contenedor con lista y barra de desplazamiento
        self.contenedor_lista_categorias = ttk.Frame(self.contenedor)
        self.lista_categorias = tk.Listbox()
        # Barra de navegación vertical
        self.scrollbar_lista_categorias = ttk.Scrollbar(self.contenedor_lista_categorias, orient=tk.VERTICAL)
        # Vincula barra vertical con lista de categorias que permite seleccion multiple
        self.lista_categorias = tk.Listbox(
            self.contenedor_lista_categorias,
            selectmode=tk.EXTENDED,
            yscrollcommand=self.scrollbar_lista_categorias.set,
            font=font.Font(family="Verdana", size=12)
        )
        self.scrollbar_lista_categorias.config(command=self.lista_categorias.yview)
        # Ubicar scrollbar a la derecha
        self.scrollbar_lista_categorias.pack(side=tk.RIGHT, fill=tk.Y)
        # Pone lista de categorias
        self.lista_categorias.pack(fill=tk.BOTH, expand=True)
        # Agrega categorías alamacenadas en la lista
        self.lista_categorias.insert(0, *self.categorias)
        # Agrega frame
        self.contenedor_lista_categorias.grid(row=3, column=0, columnspan=2, padx=10, sticky="nsew")

    def get_categories(self):
        return ("Inglés", "Soft skills", "Backend", "Frontend")

    def add_question(self):
        if self.ent_pregunta.get():
            try:
                # Tupla de indices (posiciones) del elemento (categoria) seleccionado
                indices = self.lista_categorias.curselection()
                pregunta = self.ent_pregunta.get()
                categorias = ", ".join(self.lista_categorias.get(i) for i in indices)

                if indices:
                    confirmar = messagebox.askyesno(
                        title="Agregar pregunta",
                        message= f"Se agregara {pregunta} con categoria(s): {categorias}"
                    )

                    if confirmar:
                        print(f"Agregar: {pregunta}")
                        print(f"Categorias: {categorias}")
                else:
                    messagebox.showwarning(
                        title="Atención",
                        message="Debe seleccionar al menos una categoría para la pregunta."
                    )

            except Exception as error:
                messagebox.showerror(
                    title="Atención",
                    message="Debes seleccionar al menos una categoría para la pregunta."
                )
                print(error)
        else:
            messagebox.showwarning(
                title="Atención",
                message="Debe ingresar el nombre de una categoría para agregarla"
            )

    def cancel(self):
        print("cancelar")

if __name__ == "__main__":
    root = AgregarPregunta()
    root.mainloop()