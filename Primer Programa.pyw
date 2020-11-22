from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()

root.title("Gastos Mensuales")
root.iconbitmap(r'C:\Users\ivand\Google Drive\Programación\Python\Practicas\Practica-Python\vader.ico')
root.resizable(0,0)
root.geometry("650x650")
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


root.mainloop()