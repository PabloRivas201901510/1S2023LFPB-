# EJEMPLO DE PRACTICA 1
# CURSO LENGUAJES FORMALES Y DE PROGRAMACION B-
# AUTOR: PABLO DANIEL RIVAS MARROQUIN


from carga import leerArchivoEntrada


ListaPelicualas = []

# INICIA EL PROGRAMA
print("-----------------------")
print("BINVENIDOS ESTUDIANTES")
print("-----------------------")
input()

op = 0
while op != 5:
    print("\n-----------------------")
    print("MENU PRINCIPAL")
    print("1 Carga")
    print("2 Gestion")
    print("3 Filtro")
    print("4 Grafico")
    print("5 Salir")
    print("-----------------------")
    print("1Elija una opcion de 1 a 5:")
    op = int(input())
    if op == 1:
        # CARGA DE ARCHIVOS
        print("#####CARGA DE ARCHIVOS#####")
        leerArchivoEntrada(ListaPelicualas)
        print("CARGO EXITOSAMENTE\n")
        for i in ListaPelicualas:
            i.mostarinfo()
        input()
        pass
    elif op == 2:
        # GESTION
        print("GESTION")
        pass
    elif op == 3:
        # FILTRO
        print("FILTRO")
        pass
    elif op == 4:
        # GRAFICO
        print("GRAFICO")
        pass
    elif op == 5:
        # SALIDA
        print("GRACIAS POR USAR EL PROGRAMA")
        break
