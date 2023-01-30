
lista1 =     ['a', 'b', 'w', 'd', 'e', 'f', 'g']
#posiciones    0    1    2    3    4    5    6
#inverso      -7   -6   -5   -4   -3   -2   -1

#APPEND: AGREGAR un item A LA LISTA EN LA ULTIMA POSICION
lista1.append('h')
print(lista1[:])



#EXTEND: AGREGA EL CONTENIDO DE UNA LISTA A OTRA EXISTENTE
lista2 = ['a', 'b', 'c']
lista2.extend(lista1)
print(lista2[:])

#COUNT: CONTAR LOS DATOS REPETIDOS
print('count: ', lista2.count('a'))

#INDEX: ENCONTRAR LA POSICION EN DONDE SE ENCUENTRA EL ITEM
print('index: ', lista2.index('a'))

#INSERT: AGREGA UN ITEM A LA LISTA EN UNA POSICION ESPECIFICA
lista2.insert(2, 'Z')
print('insert: ', lista2[:])

#POP: EXTRAE Y ELIMINA UN DATO DE LA LISTA
aux = lista2.pop(2)
print('pop: ', lista2[:])
print('pop: ', aux)

#REVERSE: DARLE LA VUELTA A LA LISTA
lista2.reverse()
print('reverse: ', lista2[:])

#SORT: ORDENA ASCENDENTEMENTE LOS ITEMS
lista2.sort()
print('sort: ', lista2[:])


#CLEAR: LIMPIAR LA LISTA
lista1.clear()
print('clear: ', lista1[:])



