#MANEJO DE ARCHIVOS
archivos = open('archivos/entrada1.txt', 'r')

# VAMOS A LEER EL ARCHIVO
linea = archivos.readline()
print(linea)

while linea != '':
    linea = archivos.readline()
    print(linea)
#CERRAMOS EL ARCHIVO
archivos.close()

#******************************************
#ESCRIBIR EN UN ARCHIVO
archivos = open('archivos/entrada.txt', 'w')

#ESCRIBIMOS EN EL ARCHIVO
archivos.write('\n CAMBIO')

#CERRAMOS EL ARCHIVO
archivos.close()


