from tkinter import *
from tkinter import messagebox
import tkinter as tK

#Función para validar el login
def validar():
    if entrada1.get()=="programacion2":
        abrirventana2()
    else:
        messagebox.showwarning("ADVERTENCIA", "Password incorrecto")

#Función para ingresar al menú principal.
def abrirventana2():
    ventana.withdraw()
    win=tK.Toplevel()
    menubar = Menu(win)
    win.config(menu=menubar)

    #Variables del menú deplegable
    filemenu = Menu(menubar)
    editmenu = Menu(menubar)
    helpmenu = Menu(menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir")
    filemenu.add_command(label="Guardar")
    filemenu.add_command(label="Cerrar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=win.quit)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cortar")
    editmenu.add_command(label="Copiar")
    editmenu.add_command(label="Pegar")

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Editar", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    #-----------------------------MENÚ PRINCIPAL--------------------------------------#

    win.title('BIENVENIDOS A SISTEMAS INTEGRALES TECNO-TALLER')
    win.geometry('800x500')
    win.iconbitmap("autollave.ico")
    win.configure(background='dark turquoise')
    
    encabezado2=tK.Label(win, text="Bienvenid@ a la segunda ventana", bg="black", fg="white")
    encabezado2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tK.X)
    boton2=tK.Button(win, text="SALIR", command=win.destroy)
    boton2.pack(side=tK.TOP)

def cerrarventana():
    ventana.destroy()

#---------------------------------MENÚ INICIO (PRINCIPAL)-------------------------------#
ventana=tK.Tk()
ventana.title('MENÚ INICIO')
ventana.geometry('500x500')
ventana.resizable(width=0, height=0)
ventana.iconbitmap("herramienta.ico")
fondo=PhotoImage(file='giphy2.gif')
fondo1=Label(ventana, image=fondo).place(x=1, y=1, relwidth=1, relheight=1.2)
#ventana.configure(background='dark turquoise')

encabezado1=tK.Label(ventana, text="SERVICIOS INTEGRALES TECNO-TALLER", bg="dark blue", fg="white")
encabezado1.pack(padx=5, pady=5, ipadx=5, ipady=5)
entrada1=tK.Entry(ventana)
entrada1.pack(fill=tK.X, padx=5, pady=5, ipadx=5, ipady=5)

boton1=tK.Button(ventana, text="INGRESE CON SU PASSWORD", fg="blue", command=validar)
boton1.pack(side=tK.TOP)

ventana.mainloop()