"""
Admin
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Fri 29-Nov-2024

Ventana para el administrador, le permite realizar las siguientes actividades:
- Agregar categorías
- Eliminar categorías
- Agregar preguntas
- Eliminar preguntas
"""
# Importaciones

import tkinter as tk
from tkinter import font, ttk, messagebox
from PIL import Image, ImageTk

# Importa ventanas secundarias

from agregar_pregunta import AgregarPregunta

class Categorias(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categorias = self.get_categories()

        self.nombre_categoria = ttk.Entry(
            self,
            font=font.Font(family="Verdana", size=14),
            justify=tk.CENTER,
            style="C.TEntry"
        )
        self.nombre_categoria.grid(row=0, column=0, pady=30, padx=30)

        self.agregar_categoria = ttk.Button(
            self,
            text="Agregar Categoría",
            command=self.add_category,
            style="GR.TButton"
        )
        self.agregar_categoria.grid(row=0, column=1, pady=30, padx=30)

        self.lbl_categorias = ttk.Label(
            self,
            text="Categorias",
            style="T.TLabel",
            anchor=tk.CENTER
        )
        self.lbl_categorias.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Marco contenedor con lista y barra de desplazamiento
        self.contenedor_lista_categorias = ttk.Frame(self)
        # Inicia listbox
        self.lista_categorias = tk.Listbox()

        # Barra de navegación vertical
        self.scrollbar_lista_categorias = ttk.Scrollbar(
            self.contenedor_lista_categorias,
            orient=tk.VERTICAL
        )
        # Vincula barra vertical con lista de categorias
        self.lista_categorias = tk.Listbox(
            self.contenedor_lista_categorias,
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
        self.contenedor_lista_categorias.grid(row=2, column=0, columnspan=2, padx=10, sticky="nsew")

        self.eliminar_categoria = ttk.Button(
            self,
            text="Eliminar categoría",
            command=self.delete_category,
            style="RE.TButton"
        )
        self.eliminar_categoria.grid(row=3, column=0, columnspan=2, pady=30, padx=30, sticky="ew")

    def add_category(self):
        if self.nombre_categoria.get():
            # Agrega a la lista de la UI
            self.lista_categorias.insert(tk.END, self.nombre_categoria.get())
            # Elimina el texto del campo de entrada
            self.nombre_categoria.delete(0, tk.END)
            # Avisa que se agrego la categoría
            messagebox.showinfo(
                title="Mensaje",
                message="Se agrego categoría",
                parent=self
            )
        else:
            messagebox.showwarning(
                title="Atención",
                message="Debe ingresar el nombre de una categoría para agregarla",
                parent=self
            )

    def delete_category(self):
        try:
            # Tupla de indices (posiciones) del elemento (categoria) seleccionado, en este caso solo obtiene uno
            indice = self.lista_categorias.curselection()
            categoria = self.lista_categorias.get(indice)

            confirmar = messagebox.askyesno(
                title="Borrar categoria",
                message= f"¿Estas seguro de borrar {categoria}?",
                parent=self
            )

            if confirmar:
                # Borra la categoria de la lista
                self.lista_categorias.delete(indice)
                # Avisa que se elimino la categoría
                messagebox.showinfo(
                    title="Mensaje",
                    message=f"Se elimino la categoría {categoria}",
                    parent=self
                )

        except Exception as error:
            messagebox.showerror(
                title="Error",
                message="No haz seleccionado una categoría para eliminar",
                parent=self
            )
            print(error)

    def get_categories(self):
        return ("Inglés", "Soft skills", "Backend", "Frontend")

class Preguntas(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tupla de categorias
        self.categorias = list(self.get_categories())

        # Combobox para seleccionar que categoria de preguntas se busca ver
        self.combo_categorias = ttk.Combobox(
            self,
            state="readonly",
            values=self.categorias,
            font=font.Font(family="Verdana", size=14)
        )
        # Asociando el evento de seleccion de elemento
        self.combo_categorias.bind("<<ComboboxSelected>>", self.mostrar_categoria_seleccionada)
        self.combo_categorias.grid(row=0, column=0, columnspan=2, pady=30, padx=40, sticky="ew")

        # Preguntas
        self.preguntas = self.get_questions()
        # Marco contenedor con lista y barra de desplazamiento
        self.contenedor_lista_preguntas = ttk.Frame(self, style="G.TFrame")
        self.lista_preguntas = tk.Listbox()
        # Barra de navegación vertical
        self.scrollbar_lista_preguntas = ttk.Scrollbar(self.contenedor_lista_preguntas, orient=tk.VERTICAL)
        # Vincula barra vertical con lista de preguntas
        self.lista_preguntas = tk.Listbox(
            self.contenedor_lista_preguntas,
            yscrollcommand=self.scrollbar_lista_preguntas.set,
            font=font.Font(family="Verdana", size=12),
            background="#f0f0f0"
        )
        self.scrollbar_lista_preguntas.config(command=self.lista_preguntas.yview)
        # Ubicar scrollbar a la derecha
        self.scrollbar_lista_preguntas.pack(side=tk.RIGHT, fill=tk.Y)
        # Pone lista de preguntas
        self.lista_preguntas.pack(fill=tk.BOTH, expand=True)
        # Agrega preguntas alamacenadas en la lista
        for tupla in self.preguntas:
            for elemento in tupla:
                self.lista_preguntas.insert(tk.END, elemento)
        # Agrega frame
        self.contenedor_lista_preguntas.grid(row=1, column=0, columnspan=2, padx=20, sticky="nsew")

        self.btn_agregar_pregunta = ttk.Button(
            self,
            text="Agregar pregunta",
            command=self.abrir_agregar_pregunta,
            style="GR.TButton"
        )
        self.btn_agregar_pregunta.grid(row=2, column=0, pady=20, padx=20)

        self.btn_eliminar_pregunta = ttk.Button(
            self,
            text="Eliminar pregunta",
            command=self.eliminar_pregunta,
            style="RE.TButton"
        )
        self.btn_eliminar_pregunta.grid(row=2, column=1, pady=20, padx=20)


    def get_categories(self):
        return ("Inglés", "Soft skills", "Backend", "Frontend")

    def mostrar_categoria_seleccionada(self, event):
        # Obtener la categoría seleccionada
        categoria = self.combo_categorias.get()
        messagebox.showinfo(
            message=f"Mostrar {categoria}",
            title="Mostrar categoria",
            parent=self
        )

    def get_questions(self):
        return [("¿Pregunta 1?", "Inglés, Softskills"), ("¿Pregunta 2?", "Inglés, Backend"), ("¿Pregunta 3?", "Inglés"), ("¿Pregunta 4?", "Inglés, Frontend")]

    def abrir_agregar_pregunta(self):
        if not AgregarPregunta.en_uso:
            # Crear la ventana secundaria y pasar como argumento
            # la función en la cual queremos recibir el dato
            # ingresado.
            self.ventana_agregar_pregunta = AgregarPregunta(
                callback=self.pregunta_ingresada
            )

    def eliminar_pregunta(self):
        try:
            # Tupla de indices (posiciones) del elemento (pregunta) seleccionado, en este caso solo obtiene uno
            indice = self.lista_preguntas.curselection()
            pregunta = self.lista_preguntas.get(indice)

            confirmar = messagebox.askyesno(
                title="Borrar pregunta",
                message= f"¿Estas seguro de borrar {pregunta}?",
                parent=self
            )

            if confirmar:
                # Borra la pregunta de la lista
                self.lista_preguntas.delete(indice[0], indice[0]+1)
                # Avisa que se elimino la categoría
                messagebox.showinfo(
                    title="Mensaje",
                    message=f"Se elimino la pregunta {pregunta}",
                    parent=self
                )

        except Exception as error:
            messagebox.showerror(
                title="Error",
                message="No haz seleccionado una pregunta para eliminar",
                parent=self
            )
            print(error)

    def pregunta_ingresada(self, tupla_pregunta_categorias):
        # Esta función es invocada cuando el usuario presiona el
        # botón "Agregar" de la ventana Agregar Pregunta.
        # La pregunta ingresada y sus categorías estas dentro
        # del argumento "tupla_pregunta_categorias"
        self.lista_preguntas.insert(tk.END, tupla_pregunta_categorias[0])
        self.lista_preguntas.insert(tk.END, tupla_pregunta_categorias[1])

class Admin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Administrador")

        # Estilos
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.configure("C.TEntry", foreground="black")

        self.style.configure("GR.TButton", foreground="white", font=('Verdana', 14, 'bold'), background="#66BB6A", borderwidth=0, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('GR.TButton', background=[('active', '#66BB6A')])

        self.style.configure("T.TLabel", font=('Verdana', 18, 'bold'), foreground="#1E88E5", background="#f0f0f0", padding=10)

        self.style.configure("RE.TButton", foreground="white", font=('Verdana', 14, 'bold'), background="#E57373", borderwidth=0, focusthickness=3, focuscolor='none', padding=10)
        self.style.map('RE.TButton', background=[('active', '#E57373')])

        self.style.configure("TNotebook", background="white")

        self.style.configure("TFrame", background="white")

        self.style.configure("G.TFrame", background="#f0f0f0")

        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack()

        self.Opciones = ttk.Notebook(self.contenedor, style="TNotebook")

        self.Frame_Categorias = Categorias(self.Opciones)
        self.Opciones.add(self.Frame_Categorias, text="Categorías", padding=10)

        self.Frame_Preguntas = Preguntas(self.Opciones)
        self.Opciones.add(self.Frame_Preguntas, text="Preguntas", padding=50)

        self.Opciones.pack()

if __name__ == "__main__":
    root = Admin()
    root.mainloop()