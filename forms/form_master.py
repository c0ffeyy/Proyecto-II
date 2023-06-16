# Panel principal de la aplicación:

from tkinter import *
from tkinter.font import BOLD
import utils.generic as utl

# Creamos la clase MasterPanel:
class MasterPanel:
    def __init__(self): # Constructor
        # Ventana principal:
        self.ventana = Tk()
        # Título a la ventana:
        self.ventana.title("Master panel")
        # Obtenemos el ancho y alto de la pantalla del dispositivo:
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        # Configuramos las dimensiones de la ventana para que ocupe toda la pantalla:
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        # Color de fondo de la ventana:
        self.ventana.config(bg="#fcfcfc")
        # Deshabilitamos la capacidad de redimensionar la ventana:
        self.ventana.resizable(width=0, height=0)

        # Cargamos el logo con una función de utilidad:
        logo = utl.leer_imagen("./img/logo.png", (200, 200))

        # Etiqueta con logo:
        label = Label(self.ventana, image=logo, bg="#bbd2fc")
        # Configuramos la posición y tamaño de la etiqueta para que ocupe toda la ventana:
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Bucle principal de la ventana:
        self.ventana.mainloop()