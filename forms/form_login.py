# Inicio de Sesión de la aplicación:

from tkinter import * # Módulo Tkinter
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import utils.generic as utl # Módulo local de Funciones de Utilidad
from forms.form_master import MasterPanel # Módulo local del Panel Principal

class App:
    # Método de verificación de usuario:
    def verificar(self):
        usu = self.usuario.get() # Obtenemos el usuario ingresado
        password = self.password.get() # Obtenemos la contraseña ingresada     
        if(usu == "root" and password == "1234"): # Condicional que verifica el usuario
            self.ventana.destroy() # Destruimos la ventana de Login
            MasterPanel() # Llamamos al Panel Principal de la app
        else:
            messagebox.showerror(message="Ha ingresado información incorrecta",title="Error") # Mensaje de error en caso de información incorrecta
    
    # Constructor
    def __init__(self):
        # Ventana del Login:
        self.ventana = Tk()
        # Título a la ventana:
        self.ventana.title("Inicio de sesión")
        # Tamaño a la ventana:
        self.ventana.geometry("800x500")
        # Color de fondo de la ventana:
        self.ventana.config(bg="#fcfcfc")
        # Deshabilitamos la capacidad de redimensionar la ventana:
        self.ventana.resizable(width=0, height=0)
        # Centramos la ventana con una función de utilidad:
        utl.centrar_ventana(self.ventana, 800, 500)

        # Cargamos el logo con una función de utilidad:
        logo = utl.leer_imagen("./img/logo.png", (200, 200))

        # Marco de logo:
        frame_logo = Frame(self.ventana, bd=0, width=300, relief=SOLID, padx=10, pady=10, bg="#bbd2fc")
        frame_logo.pack(side="left", expand=NO, fill=BOTH)
        label = Label(frame_logo, image=logo, bg="#bbd2fc")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Marco de formulario:
        frame_form = Frame(self.ventana, bd=0, relief=SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=YES, fill=BOTH)

        # Marco de formulario de arriba:
        frame_form_top = Frame(frame_form, height=50, bd=0, relief=SOLID, bg="black")
        frame_form_top.pack(side="top", fill=X)
        titulo = Label(frame_form_top, text="Inicio de sesión", font=("Times", 30), fg="#666a88", bg="#fcfcfc", pady=50)
        titulo.pack(expand=YES, fill=BOTH)

        # Marco de formulario de relleno:
        frame_form_fill = Frame(frame_form,height = 50,  bd=0, relief=SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=YES,fill=BOTH)

        # - Etiqueta de Usuario:
        etiqueta_usuario = Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=X, padx=20,pady=5)
        # - Entrada de Usuario:
        self.usuario = Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=X, padx=20,pady=10)

        # - Etiqueta de Contraseña:
        etiqueta_password = Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=X, padx=20,pady=5)
        # - Entrada de Contraseña:
        self.password = Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=X, padx=20,pady=10)
        self.password.config(show="*")

        # Botón de inicio:
        inicio = Button(frame_form_fill,text="Iniciar sesión",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))

        # Bucle principal de la ventana:
        self.ventana.mainloop()