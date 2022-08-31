from tkinter import *
import hashlib


WIDTH = 500
HEIGHT = 200


def encript_text(data, finish):
    key = data.get()
    md5 = hashlib.md5(key.encode()) 

    result = md5.hexdigest()
    finish.set(result)

def main():
    
    ventana = Tk(className='Software encriptador md5 md5thon 1.0')
    ventana.geometry(f"{WIDTH}x{HEIGHT}")
    ventana.minsize(500,HEIGHT)
    ventana.maxsize(500,HEIGHT)
    Label(ventana, text="Texto para Codificar").pack()

    str_enctript = StringVar()


    Label(ventana, text="Ingresa el Texto").place(x=205, y=50)
    Entry(ventana, textvariable = str_enctript).place(x=190, y=70)
    Label(ventana, text="Resultado Encriptado").place(x=205, y=90)

    str_finish = StringVar()

    Entry(ventana, textvariable = str_finish, width=40).place(x=130, y=110)
    Button(ventana, text="Encriptar", command=lambda:encript_text(str_enctript, str_finish)).place(x=220, y=140)




    ventana.mainloop()





if __name__ == '__main__':
   
    main()