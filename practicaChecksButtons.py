from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montaña=IntVar()
turismo=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if (playa.get()==1):
        opcionEscogida+="playa"

    if (montaña.get()==1):
        opcionEscogida+="Montaña"
        
    if (turismo.get()==1):
        opcionEscogida+="Turismo"    

    textoFinal.config(text=opcionEscogida)

# imagen1=PhotoImage(file="foto.jpg")
# Label(root, image=imagen1).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige Destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()