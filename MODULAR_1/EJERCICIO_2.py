"""2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.)."""



lista=[5, 6, 7, 5, 8, 0, 2, 3, 4, 1]
# IZQUIERDA - DERECHA -1, -2, -3 
# DERECHA - IZQUIERDA 0, 1, 2, 3 


def obtenerLista(lista,posicion):
    listaNueva = lista[-1:] + lista[:-1] #concatena la lista y rotamos la lista hacia la derecha ubicandose el -1 como nuestro primer numero
    return listaNueva 
print(obtenerLista(lista,-1))