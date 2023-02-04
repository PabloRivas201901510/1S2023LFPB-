## TKINTER

import tkinter as tk

### METODO DEL BOTON1
#                 STRINGVAR ETIQUETA,   GET STRINGVAR LABEL
def evento_boton1(text:tk.StringVar,        texto):
    text.set(texto)

# CREAR UNA VENTANA
ventana = tk.Tk()

# ASIGNAMOS UN TAMAÑO A LA VENTANA
ventana.geometry('800x600')

# AGREGAR UN TITULO
ventana.title("Ejemplo de laboratorio de lenguajes formales y programacion")


# ETIQUETA
etiqueta1 = tk.Label(ventana, text="CARNET", font=("Arial Black", 20), fg="Blue")
etiqueta1.place(x=100 , y=100)

etiqueta2 = tk.Label(ventana, text="NOMBRE", font=("Arial Black", 20), fg="Red")
etiqueta2.place(x=100 , y=200)

# ETIQUETA DINAMICA
texto = tk.StringVar()
texto.set("ASIGNADO")
etiqueta3 = tk.Label(ventana, textvariable=texto, font=("Arial Black", 20), fg="Green")
etiqueta3.place(x=100 , y=300)



# ENTRADAS
text_entrada1 = tk.StringVar()
entrada1 = tk.Entry(ventana, textvariable= text_entrada1, font=("Arial Black", 16))
entrada1.place(x=300 , y=100)


# BOTONES
boton1 = tk.Button(ventana, text="Enviar", font=("Arial Black", 16), command=lambda:evento_boton1(texto, text_entrada1.get()))
boton1.place(x=600 , y=400)



# MOSTAR LA VENTANA
ventana.mainloop()
