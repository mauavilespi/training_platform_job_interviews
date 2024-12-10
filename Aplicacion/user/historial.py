"""
Historial de reportes
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Sat 30-Nov-2024

Aqui el usuario podra ver la lista de reportes que ha podido ir almacenando
puede seleccionar un reporte, esto lo redireccionara a la ventana: Ver Reporte
"""
# Importaciones
import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import os # Para obtener la lista de reportes

# Importa ventana Ver Reporte
from ver_reporte import VerReporte

class Historial(tk.Toplevel):

    # Atributo de la clase que indica si la ventana secundaria está en uso.
    en_uso = False

    def __init__(self):
        super().__init__()
        self.title("Historial de reportes")
        self.config(background="white")

        #  -------------- Estilos -------------- #
        self.style = ttk.Style()
        self.style.theme_use('alt')

        # Titulo de seccion: "Reportes"
        self.style.configure(
            "BG.TLabel",
            font=('Verdana bold', 18),
            foreground="black",
            background="#f0f0f0",
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
        self.style.map('B.TButton', background=[('active', '#f0f0f0')], foreground=[('active', 'gray')])

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

        # Imagen para boton "Volver al inicio"
        self.img_volver = tk.PhotoImage(file="/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/Aplicacion/user/assets/homeicon.png")

        # -------------- Componentes -------------- #
        # Frame contenedor (Pone fondo en blanco)
        self.contenedor = ttk.Frame(self, style="TFrame")
        self.contenedor.pack(padx=50, pady=25)

        # Boton: Volver al inicio
        self.volver = ttk.Button(
            self.contenedor,
            image=self.img_volver,
            compound=tk.LEFT,
            text=" Volver al inicio",
            style="B.TButton",
            command=self.goback
        )
        self.volver.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Label: Titulo "Reportes guardados"
        self.titulo = ttk.Label(
            self.contenedor,
            text="Reportes guardados",
            style="BG.TLabel",
            anchor=tk.CENTER
        )
        self.titulo.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Frame: Marco para contener la lista de reportes
        self.contenedorLista = ttk.Frame(self.contenedor)
        # ListBox: Lista de reportes
        self.reportes = tk.Listbox()

        # Crear una barra de deslizamiento con orientación vertical.
        self.scrollbar = ttk.Scrollbar(
            self.contenedorLista,
            orient=tk.VERTICAL
        )
        # Vincular scrollbar y configurar la lista.
        self.reportes = tk.Listbox(
            self.contenedorLista,
            yscrollcommand=self.scrollbar.set,
            font=font.Font(family="Verdana", size=12)
        )
        self.scrollbar.config(command=self.reportes.yview)
        # Ubicar scrollbar a la derecha.
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Ubicar lista a la izquierda
        self.reportes.pack(expand=True, fill=tk.BOTH)

        # Insertar elementos.
        for reporte in self.get_reportes():
            self.reportes.insert(tk.END, reporte.replace("_", ":"))

        self.contenedorLista.grid(row=2, column=0, sticky="nsew", pady=10, ipadx=80)

        # Boton: Abrir
        self.Abrir=ttk.Button(
            self.contenedor,
            text="Abrir",
            command=self.abrir_ventana_reporte,
            style="A.TButton"
        )
        self.Abrir.grid(row=4, column=0, sticky="nsew", pady=10, padx=10)

        # Para que la ventana secundaria obtenga el foco automáticamente una vez creada
        self.focus()
        # El usuario no pueda utilizar la ventana de administrador mientras esta ventana está visible
        self.grab_set()
        # Indicar que la ventana está en uso luego de crearse.
        self.__class__.en_uso = True

    def get_reportes(self):
        archivos = os.listdir("/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/reports/")
        archivos = [nombre_archivo[:-4] for nombre_archivo in archivos if os.path.isfile("/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/reports/"+nombre_archivo)]
        # print(archivos)
        return archivos

    def goback(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()

    def abrir_ventana_reporte(self):
        try:
            # Tupla de indices (posiciones) del elemento (reporte) seleccionado, en este caso solo obtiene uno
            indice = self.reportes.curselection()
            reporte = self.reportes.get(indice).replace(":", "_")

            if not VerReporte.en_uso:
                # Crear la ventana secundaria y pasar como argumento
                # la función en la cual queremos recibir el dato
                # ingresado.
                # print(reporte+".csv")
                self.ventana_ver_reporte = VerReporte(
                    # Se envia el nombre con la extensión .csv
                    # para poder acceder al archivo donde esta el reporte
                    nombre_reporte=reporte+".csv",
                    indice_reporte=indice,
                    callback=self.eliminar_reporte
                )

        except Exception as error:
            messagebox.showerror(
                title="Error",
                message="No haz seleccionado un reporte",
                parent=self
            )
            print(error)

    def eliminar_reporte(self, indice_reporte, nombre_reporte):
        # print(indice_reporte)
        indice = self.reportes.get(indice_reporte)
        # Borra el reporte de la lista
        self.reportes.delete(indice[0])
        # Borra el archivo con el reporte
        if os.path.exists("/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/reports/" + nombre_reporte):
            os.remove("/Users/mauavilespi/Documents/TTR/training_platform_job_interviews/reports/" + nombre_reporte)
        else:
            print("No existe el archivo")

if __name__ == "__main__":
    root = Historial()
    root.mainloop()