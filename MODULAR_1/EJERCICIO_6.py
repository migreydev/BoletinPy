""""6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario."""

lista=[1 ,2 ,3]

def estaOrdenada(lista):
    return True
print(estaOrdenada(lista))


def estaDesordenada(lista):
    lista.reverse()
    return False
print(estaDesordenada(lista))
