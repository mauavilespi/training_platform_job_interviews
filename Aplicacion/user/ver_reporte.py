"""
Ver Reporte
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Sun 01-Dec-2024

Se despliega el reporte de la entrevista en formato de tabla
"""

# Importaciones

import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class VerReporte(tk.Toplevel):

    # Atributo de la clase que indica si la ventana secundaria está en uso.
    en_uso = False

    def __init__(self,  *args, nombre_reporte, indice_reporte, callback=None, **kwargs):
        # Ventana
        super().__init__(*args, **kwargs)
        # callback es una función que esta ventana llamará
        # una vez presionado el botón para comunicarle el reporte a eliminar
        # (si es que se elimina)
        self.callback = callback
        # Inicializando el nombre del reporte
        self.nombre_reporte = nombre_reporte
        # print(self.nombre_reporte)
        # Inicializando el indice el reporte en la lista del historial de rpeortes
        self.indice_reporte = indice_reporte

        self.title("Inside Out")
        self.config(background="white")

        #  -------------- Estilos -------------- #
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.configure(
            "TLabel",
            font=('Verdana', 18, "bold"),
            foreground="#1E88E5",
            background="#f0f0f0",
            padding=10, relief="flat"
        )

        self.style.configure(
            "VO.TButton",
            foreground="white",
            font=('Verdana', 14),
            background="#1E88E5",
            borderwidth=0,
            focusthickness=3,
            focuscolor='none',
            padding=10
        )
        self.style.map('VO.TButton', background=[('active', '#1E88E5')])

        self.style.configure(
            "EL.TButton",
            foreground="white",
            font=('Verdana', 14),
            background="#E57373",
            borderwidth=0,
            focusthickness=3,
            focuscolor='none',
            padding=10
        )
        self.style.map('EL.TButton', background=[('active', '#E57373')])

        self.style.configure("TFrame", background="white")

        self.style.configure(
            "Treeview",
            foreground="black",
            background="white",
            font=('Verdana', 12),
            padding=10
        )

        self.style.configure(
            "Treeview.Heading",
            foreground="black",
            background="white",
            font=('Verdana', 15),
            padding=12
        )
        self.style.map(
            "Treeview.Heading",
            background=[('active', 'white')]
        )

        # Obtener imagenes para las emociones
        self.emo_disgusto = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/disgusto-s.png")
        self.emo_enojo = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/enojo-s.png")
        self.emo_feliz = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/feliz-s.png")
        self.emo_miedo = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/miedo-s.png")
        self.emo_neutral = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/neutral-s.png")
        self.emo_sorpresa = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/sorpresa-s.png")
        self.emo_triste = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/emociones/triste-s.png")

        # -------------- Componentes -------------- #
        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack(padx=25, pady=25)

        titulo_limpio = self.nombre_reporte[:-4] # Quita la extension ".csv"
        # Titulo del reporte
        self.titulo = ttk.Label(
            self.contenedor,
            text= titulo_limpio.replace("_",":"), # Cambia '_' por ':'
            anchor=tk.CENTER
        )
        self.titulo.grid(row=0, column=0, columnspan=2, sticky="we")

        # Contenedor para la tabla y la scrollbar
        self.contenedor_tabla_reporte = ttk.Frame(self.contenedor)
        # Treeview: Tabla con Reporte
        self.tablareporte = ttk.Treeview()
        # Scrollbar
        self.scrollY = ttk.Scrollbar(
            self.contenedor_tabla_reporte,
            orient=tk.VERTICAL
        )
        # Tabla de reporte (Treeview con varias columnas)
        self.tablareporte = ttk.Treeview(
            self.contenedor_tabla_reporte,
            columns=("Enojo", "Disgusto", "Miedo", "Feliz", "Neutro", "Sorpresa", "Triste"),
            yscrollcommand=self.scrollY.set
        )
        # Vincula barra vertical
        self.scrollY.config(
            command=self.tablareporte.yview
        )
        # Configurando columnas
        self.tablareporte.column("#0", width=400, anchor=tk.W)
        self.tablareporte.column("Enojo", width=140, anchor=tk.CENTER)
        self.tablareporte.column("Disgusto", width=170, anchor=tk.CENTER, stretch=tk.YES)
        self.tablareporte.column("Miedo", width=130, anchor=tk.CENTER)
        self.tablareporte.column("Feliz", width=125, anchor=tk.CENTER)
        self.tablareporte.column("Neutro", width=145, anchor=tk.CENTER)
        self.tablareporte.column("Sorpresa", width=160, anchor=tk.CENTER)
        self.tablareporte.column("Triste", width=130, anchor=tk.CENTER)
        # Titulo de de columnas
        self.tablareporte.heading("#0", text="Pregunta")
        self.tablareporte.heading("Enojo", text="Enojo", image=self.emo_enojo)
        self.tablareporte.heading("Disgusto", text="Disgusto", image=self.emo_disgusto)
        self.tablareporte.heading("Miedo", text="Miedo", image=self.emo_miedo)
        self.tablareporte.heading("Feliz", text="Feliz", image=self.emo_feliz)
        self.tablareporte.heading("Neutro", text="Neutro", image=self.emo_neutral)
        self.tablareporte.heading("Sorpresa", text="Sorpresa", image=self.emo_sorpresa)
        self.tablareporte.heading("Triste", text="Triste", image=self.emo_triste)
        # Inserta elementos
        for pregunta in self.get_reporte():
            # print(pregunta)
            self.tablareporte.insert(
                "",
                tk.END,
                text=pregunta['Preguntas'],
                values=(
                    pregunta['Enojo'],
                    pregunta['Disgusto'],
                    pregunta['Miedo'],
                    pregunta['Feliz'],
                    pregunta['Neutro'],
                    pregunta['Sorpresa'],
                    pregunta['Triste']
                )
            )
        # Obteniendo valor de las columnas de un elemento
        # print(self.tablareporte.set(self.elemento))
        # Obteniendo el valor de una columna específica
        # print(self.tablareporte.set(self.elemento, "Disgusto"))
        # Estableciendo un nuevo valor (Cambia 5 % pot 10%)
        # print(self.tablareporte.set(self.elemento, "Neutro", "10%"))

        # Agrega y ubica scrollbar
        self.scrollY.pack(side=tk.RIGHT, fill=tk.Y)

        # Agrega tabla reporte
        self.tablareporte.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        # Agrega frame
        self.contenedor_tabla_reporte.grid(row=1, column=0, columnspan=2, padx=10, sticky="nsew")

        # Boton: Eliminar
        self.Eliminar=ttk.Button(
            self.contenedor,
            text="Eliminar",
            command=self.eliminar_reporte,
            style="EL.TButton"
        )
        self.Eliminar.grid(row=2, column=0, pady=10, sticky="we")

        # Boton: Volver
        self.Volver=ttk.Button(
            self.contenedor,
            text="Volver",
            command=self.goback,
            style="VO.TButton"
        )
        self.Volver.grid(row=2, column=1, pady=10, sticky="we")

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

    def get_reporte(self):
        # Se abre el reporte en modo lectura
        with open(f"/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/reports/{self.nombre_reporte}", 'r', encoding='UTF-8') as csvfile:
            # Lee archivo tomando como delimitador las comas ','
            reader = csv.reader(csvfile, delimiter=',')
            # Se extraen encabezados
            header = next(reader)
            # Lista para guardar datos
            data = []
            # Se lee fila por fila
            for row in reader:
                # Union de encabezado con fila en una lista de tuplas: (Columna, Valor)
                iterable = zip(header, row)
                # Se pasa a diccionario
                report_dict = {key: value for key, value in iterable}
                # Se agrega el diccionario a la lista
                data.append(report_dict)

        return data

    def eliminar_reporte(self):
        confirmar = messagebox.askyesno(
            title="Borrar reporte",
            message= f"¿Estas seguro de borrar {self.nombre_reporte}?",
            parent=self
        )
        if confirmar:
            # print(f"Borrar: {self.nombre_reporte}")
            # Obtener el indice del reporte y llamar a la función
            # especificada al crear esta ventana.
            self.callback(
                self.indice_reporte,
                self.nombre_reporte
            )
            # Restablecer el atributo al cerrarse.
            self.__class__.en_uso = False
            # Cerrar la ventana.
            self.destroy()
            # Restablecer el atributo al cerrarse.
            self.__class__.en_uso = False
            return super().destroy()


if __name__ == "__main__":
    root = VerReporte()
    root.mainloop()