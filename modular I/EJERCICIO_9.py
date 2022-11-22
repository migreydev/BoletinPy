"""9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k."""

lista=[2, 4, 50, 12, 1, 5, 9, 8, 24, 15 ]
listaMenor=[]
listaMayor=[]
listaMultiplo=[]
multiplo=0
k= 6
i=0

# a) Devolver una lista de números con los menores de k


def obtenerMenor(lista):
    i=0
    while i <= len(lista):
        if k >= (lista[i-1]):
            listaMenor.append(lista[i-1])
        i += 1
    return listaMenor

def obtenerMayor(lista):
    i=0
    while i <= len(lista):
        if k <= (lista[i-1]):
            listaMayor.append(lista[i-1])
        i += 1
    return listaMayor


def obtenerMultiplo(lista):
    i=0
    for i in lista:
        if i%k==0:
            listaMultiplo.append(i)
    i+=1
    return listaMultiplo

print(obtenerMenor(lista))
print(obtenerMayor(lista))
print(obtenerMultiplo(lista))

