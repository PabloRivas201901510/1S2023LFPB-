
_token = "Operacion"

_text = """ 
{
    "Operacion":"Suma"
    "Valor1":4.5
    "Valor2":5.32
}
"""
def analizar(token, text):
    count = 0
    tmp = 0
    token_tmp = ""
    for i in text:
        # CUANDO LA LETRA HAGA MATCH CON EL TOKEN ENTRA
        #print(tmp)
        if i == token[tmp]:
            if 0 == tmp:
                start = count
            tmp += 1
            token_tmp += i
            if len(token) == tmp:
                tmp = 0
                print('ENCONTRADA -> ', token_tmp,' | INICIO -> ', start, ' | FINAL -> ', count)
                token_tmp = ""
                
        else:
            tmp = 0
            token_tmp = ""
        count+=1
        

analizar("Operacion",_text)
analizar("Suma",_text)
analizar("\"",_text)