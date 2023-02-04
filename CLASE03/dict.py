# DICCIONARIO VACIO
diccionario = {}

# DICCIONARIO CON DATOS AL INICIO
diccionario = {1:"Perro", 2:"Gato", 3:"Pez"}

print(diccionario[1])
print(diccionario[2])
print(diccionario[3])
print(diccionario)

diccionario[4] = "Tortuga"

print(diccionario)

print("\n------------------------\n")
## ITERAR LISTA CON FOR
lista1 = ["a", "e", "i", "o", "u"]
for i in lista1:
    print(i)

print("\n------------------------\n")
## ITERAR LISTA CON WHILE
count = 0
while count < len(lista1):
    print(lista1[count])
    count += 1

print("\n------------------------\n")
## LISTA DE DICCIONARIOS
form = [{"carne":201901510, "nombre":"Pablo Rivas"},
        {"carne":201901689, "nombre":"Alejandro Juarez"},
        {"carne":201920655, "nombre":"Daniela Perez"}
        ]
for i in form:
    print(i["nombre"])


print("\n------------------------\n")
## ITERAR DICCIONARIO CON CLAVE VALOR
diccionario = {1:"Perro", 2:"Gato", 3:"Pez"}
for key, value in diccionario.items():
    print(key, value)

## ITERAR DICCIONARIO CON CLAVE 
print("\n------------------------\n")
for key in diccionario:
    print(key)

## ITERAR DICCIONARIO CON VALOR
print("\n------------------------\n")
for value in diccionario.values():
    print(value)


