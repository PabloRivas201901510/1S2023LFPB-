import os



archivo = open("entrada.txt", 'r')
lineas = archivo.readlines()

listaDatos = []
for i in lineas:
    i = i.replace('\n','')
    i = i.split(",")
    x = {"producto":i[0],"sucursal":i[1], "fecha":i[2]}
    listaDatos.append(x)

print(listaDatos)
archivo.close()



archivoDOT = open("imagen.dot","w")
archivoDOT.write("digraph { \n")
archivoDOT.write('rankdir = LR \n' )
archivoDOT.write('node[shape=record, fontname="Arial Black", fontsize=16] \n')
for i in listaDatos:
    archivoDOT.write(i["sucursal"]+'[color=blue, style=filled, label="'+i["sucursal"] +'|'+ i["fecha"]+'"]\n')

for i in listaDatos:
    archivoDOT.write(i["sucursal"]+'->'+i["producto"] + "\n")

archivoDOT.write("} \n")

archivoDOT.close()

os.system("dot.exe -Tpng imagen.dot -o  ReporteGrafico.png")