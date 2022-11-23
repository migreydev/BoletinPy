"""5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]."""

lista=['Di', 'buen', 'dia', 'a', 'papa']
listaReverse=[]
#listaReverse= ['papa', 'a', ‘día’, ‘buen’, ‘Di’]


def obtenerOriginal (lista):
    return lista
print(obtenerOriginal(lista))


def obtenerInvertida(lista):
    for i in range(len(lista)):
        if listaReverse==lista[::-1]:
            listaReverse.append(lista)
    return listaReverse
print(obtenerInvertida(lista))

lista=['Di', 'buen', 'dia', 'a', 'papa']
invertida = []


for i in lista:
    invertida= [i] + invertida
    
print(invertida)