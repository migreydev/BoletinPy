"""1. Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números"""


print("EJERCICIO A")
from random import randint

lista = []

for i in range(100):
    lista.append(randint(0,100))
print(lista)

def obtenerElementoMayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor
print(obtenerElementoMayor(lista))

print("EJERCICIO B")
from random import randint

lista = []

for i in range(100):
    lista.append(randint(0,100))
print(lista)

def obtenerElementoMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor
print(obtenerElementoMenor(lista))


print("EJERCICIO C")
from random import randint  

lista=[]
for i in range(10):
    lista.append(randint(0,10))
print(lista)

def obtenerSumatorio(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma
print(obtenerSumatorio(lista))

print("EJERCICIO D")
from random import randint

lista=[]

for i in range(10):
    lista.append(randint(0,10))
print(lista)

def obtenerMedia(lista):
    media=sum(lista)/len(lista)
    return media
print(obtenerMedia(lista))

print("EJERCICIO E")

from random import randint

lista=[]

for i in range(10):
    lista.append(randint(0,10))
print(lista)

def obtenerSustituto(lista, numeroSustituto, numeroActual):
    for i in range(len(lista)):
        if numeroSustituto==lista[i]:
           lista[i]=numeroActual
    return lista
print(obtenerSustituto(lista, 5, 7))

print("EJERCICIO F")

from random import randint

lista=[]

for i in range(100):
    lista.append(randint(0,100))
print(lista)

def obtenerNumeros(lista):
    return lista
print(obtenerNumeros(lista))

    