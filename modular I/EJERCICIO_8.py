"""8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números."""

print("A")

# 2, 3, 5, 7, 11, 13, 17, 19, 23... Los números primos son aquellos que son divisibles entre ellos mismo y el 1.
 
listaPrimo=[]
lista=[]        
numero=int(input("Ingresa un número (negativo para finalizar): "))

def es_primo(numero, listaPrimo):
    while 0 < numero:
        lista.append(numero)
        for i in range(2, numero):
            if numero%i == 0:
                numero=int(input("Ingresa un número (negativo para finalizar): "))
        listaPrimo.append(numero)
        numero=int(input("Ingresa un número (negativo para finalizar): "))
    return listaPrimo

print("B")

lista=[]
suma=0
numeros=int(input("Ingresa un número (negativo para finalizar): "))

while numeros > 0:
    lista.append(numeros)
    numeros=int(input("Ingresa un número (negativo para finalizar): "))
    
def obtenerSumatorio(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma

print("C")

def obtenerMedia(lista):
    media=sum(lista)/len(lista)
    return media

print(es_primo(numero, listaPrimo))
print(obtenerSumatorio(lista))
print(obtenerMedia(lista))

print("D")


    
        
        