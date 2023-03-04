# EXPRESIONES REGULARES

import re




#CREAR UN PATRON
patron = re.compile(r'foo bar')

text = """ bar foo bar
foo barbar foo
foofoo foo bar
"""

# SEARCH -> nos devuelve la coincidencia en cualquier ubicacion
s = patron.search(text)
print('search -> ', s)

#FINDALL -> nos devuelve una lista con todas las coincidencias, solo con los caracteres
fall = patron.findall(text)
print('findall -> ', fall , len(fall))

#FINDINTER -> nos devuelve una lista con todas las coincidencias, pero con sus atributos
finter = patron.finditer(text)
print('finditer -> ', finter)

# GROUP() -> devuelve la coincidencia con la expresion regular
# START() -> devuelve la posicion inicial de la coincidencia
# END()   -> devuelve la posicion final de la coincidencia
# SPAN()  -> devuelve el rango de la coincidencia (posicion inicial y final)
for i in finter:
    print('\n',i)
    print('GROUP() -> ',i.group(), ' | START() -> ', i.start(), ' | END()   -> ', i.end(), ' | SPAN()  -> ', i.span())
