from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismo=IntVar()

def opcionesViaje()

    opcionEscogida=""

    if (playa.get()==1):
        opcionEscogida+="playa"

    if (montagna.get()==1):
        opcionEscogida+="montaña"
        
    if (turismo.get()==1):
        opcionEscogida+="turismo"    

    textoFinal.config(text=opcionEscogida)

# imagen1=PhotoImage(file="foto.jpg")
# Label(root, image=imagen1).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige Destinos", width=50).pack()

Checkbutton(frame, text="Playa").pack()
Checkbutton(frame, text="Montaña").pack()
Checkbutton(frame, text="Turismo").pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()