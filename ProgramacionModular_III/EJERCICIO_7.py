'''
7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase
y deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla
por la tercera.
'''
frase="hola que estas haciendo"
palabra="haciendo"
reemplazo="leyendo"


def reemplazar(frase, palabra, reemplazo):
    contador=0
    resultado, tmp = "", ""
    
    for i in range(len(frase)):
        if frase[i]== palabra[contador]:  
            if contador==len(palabra)-1:
                tmp="" 
                resultado+=reemplazo
                contador=0
            else:
                tmp+=frase[i]
                contador+=1
        else:
            resultado+=tmp+frase[i]
            contador=0
            tmp=""
            
    return resultado

print(reemplazar(frase, palabra, reemplazo))
