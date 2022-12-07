'''
8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una
palabra o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
'''
palabra= "hola"

def obtenerVocal(palabra):
    listaVocal=[]
    for i in range(len(palabra)):
        if palabra[i] in "aeiou":
            listaVocal.append(palabra[i])
    return listaVocal

print(obtenerVocal(palabra))
            