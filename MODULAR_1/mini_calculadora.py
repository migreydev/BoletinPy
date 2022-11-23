# procesamiento
def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    return a/b

# interfaz de entrada

def pidoDatos():
    operacion = input("+-*/")
    num1 = int(input("número 1"))
    num2 = int(input("número 2"))
    
    return [operacion, num1, num2]

# interfaz de salida
def mostrarResultado(operacion, n1, n2):
    if operacion=='+':
        print(suma(n1, n2))
    elif operacion == "-":
        print(resta(n1, n2))
    elif operacion == "*":
        print(multiplicacion(n1, n2))
    elif operacion == "/":
        print(division(n1, n2))
    return "Adiós"
    
datos = pidoDatos()
op, n_1, n_2 =  datos[0], datos[1], datos[2]
mostrarResultado(op, n_1, n_2)



def desplazar_una_posicion_derecha(lista):
    a_borrar, a_escribir = 0, lista[0]
    
    for i in range(len(lista)):
        a_borrar = lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=a_escribir
        a_escribir = a_borrar
    
    return lista


  
def desplazar(lista):
    a_escribir = lista[0]
    a_guardar = 0
    
    for i in range(len(lista)):
        if i == len(lista)-1:
            lista[0]= a_escribir
        else:
            a_guardar = lista[(i+1)]
            lista[(i+1)]= a_escribir
            a_escribir = a_guardar
    
    return (lista)

lista_numeros = [0, 1, 2, 3]
print(desplazar(["a", "b", "c"]))
print(desplazar(lista_numeros))
  
