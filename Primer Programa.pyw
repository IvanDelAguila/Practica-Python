from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkcalendar import *

root=Tk()

root.title("Gastos Mensuales")
root.iconbitmap(r'C:\Users\ivand\Google Drive\Programación\Python\Practicas\Practica-Python\vader.ico')
root.resizable(0,0)
root.geometry("715x500")

MainFrame = Frame(root, bd=10, width=715, height=500, relief=RIDGE, bg="cadetblue")
MainFrame.grid()
   
#Etiqueta Mes

label = Label(text="MES", bg="red", padx=58,).place(x=50, y=20)

#Combobox Meses

combo = ttk.Combobox(root)
combo.place(x=50, y=50)
combo['values']=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

#Etiqueta Gasto Comun

label1 = Label(text="GASTO COMUN", bg="red", padx=27).place(x=230, y=20)

#Combobox Meses

combo1 = ttk.Combobox(root)
combo1.place(x=230, y=50)
combo1['values']=('Agua', 'Luz', 'Internet', 'Arriendo', 'Celulares', 'Televisión', 'CAE')

#Etiqueta Fecha de Pago

label2 = Label(text="FECHA DE PAGO", bg="red").place(x=410, y=20)

#Cuadro Fecha de Pago

cuadro = DateEntry(root, date_pattern='dd/mm/yy', justify="center").place(x=410, y=50)

#Etiqueta Monto 

label3 = Label(text="MONTO", bg="red", padx=38).place(x=540, y=20)

#Cuadro Monto Pagado

cuadro1 = Entry(root)
cuadro1.place(x=540, y=50)

#Botones 

botonGuardar = Button(root, text="Guardar").place(x=95, y=85)

botonEliminar = Button(root, text="Eliminar").place(x=270, y=85)

botonEditar= Button(root, text="Editar").place(x=430, y=85)

root.mainloop()