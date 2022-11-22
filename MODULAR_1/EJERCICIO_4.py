"""4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares."""


lista=[]
listaPar=[]
numero=int(input("Ingresa un número (negativo para finalizar): "))
mayor= numero

def obtenerPar(listaPar):
    while numero > 0:
        lista.append(numero)
    if numero%2==0:
        listaPar.append(numero)
    return (listaPar)
  
print(obtenerPar(listaPar))

def obtenerMayor(lista):
    if numero>mayor:
        mayor=numero
        numero=int(input("Ingresa un número (negativo para finalizar): "))
    return mayor
print(obtenerMayor(lista))