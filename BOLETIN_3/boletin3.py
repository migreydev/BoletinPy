""" 1. Realizar un programa que lea un número entero por teclado e informe de si
el número es par o impar (el cero se considera par). """

numeroEntero = int(input("Dí un número"))

if numeroEntero%2 == 0 : #CON EL COMANDO % SACAMOS LOS IMPARES Y PARES
    print("El numero", numeroEntero , "entero es par")
    
else:
    print("El numero" ,numeroEntero, "entero es impar")
   
   

numeroEntero = int(input("Dí un número"))

if numeroEntero%2 == 0 : #CON EL COMANDO % SACAMOS LOS IMPARES Y PARES
    print("El numero %s entero es par" % (numeroEntero))
    
else:
    print("El numero %s entero es impar" % (numeroEntero)) 
    
print("-------------")  
    

"""2. Realizar un programa que solicite dos números por teclado e imprima en
pantalla si son iguales, el primero mayor que el segundo o el primero más
pequeño que el segundo."""


numeroUno = int(input("Di numero 1 "))
numeroDos = int(input("Di numero 2 "))

if numeroUno == numeroDos:
    print("Son iguales")
    
elif numeroUno > numeroDos:
    print("Numero %s es mayor" %(numeroUno))
    
else:
    print("Numero %s es mayor" %(numeroDos))
    

print ("-------------")   
    

"""3. Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje."""


numero = int(input("Di un numero"))

if numero%2 == 0 and numero%3 == 0:
    print("El número %s es multiplo de 2 y 3" %(numero))

elif numero%2 == 0:
    print("El número %s es multiplo de 2" %(numero))
    
elif numero%3 == 0:
    print("El número %s es multiplo de 3" %(numero))
    

print ("-------------")  


"""4. Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto."""

edad = int(input("¿Cual es tu edad?"))

if edad >= 0 and edad <=12:
    print("Tu edad es de un niño")

elif edad >= 13 and edad <=17:
    print("Tu edad es la de un adolescente")
    
elif edad >= 18 and edad <=29:
    print("Tu edad es la de un joven")
    
else:
    print("Tu edad es la de un adulto")
    
print ("-------------")          
    

"""5. Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media."""

numero1 = int(input("Di un numero "))
numero2 = int(input("Di segundo numero "))
numero3 = int(input("Di tercer numero "))
numero4 = int(input("Di cuarto numero "))

media = ((numero1 + numero2 + numero3 + numero4)/4)
print((numero1 + numero2 + numero3 + numero4)/4)
print("La media es %s" %(media))

if numero1 > media: 
    print("El primer numero es mayor a la media")
if numero2 > media:
    print("El segundo numero es mayor a la media")
    
if numero3 > media: 
    print("El tercer numero es mayor a la media")
    
if numero4 > media:
    print("El cuarto numero es mayor a la media")
    
    
  
print ("-------------")

    
"""6. Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc."""

letra = input("Escriba un solo caracter: ")

if letra == "a" or letra == "A":
    print("%s es la primera vocal" %(letra))
elif letra == "e"or letra == "E":
    print("%s es la segunda vocal" %(letra))
elif letra == "i"or letra == "I": 
    print("%s es la tercera vocal" %(letra))
elif letra == "o"or letra == "O":
    print("%s es la cuarta vocal" %(letra))
elif letra == "u"or letra == "U":
    print("%s es la quinta vocal" %(letra))

else:
    print("No es una vocal")


print ("-------------")


""""7. Realizar un programa que lea el estado civil de una persona (S-Soltero, CCasado,
V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%"""

estadoCivil = str(input("¿Introduce tu estado civil? "))
edad = int(input("Dime tu edad"))

if not(estadoCivil != "S" and estadoCivil != "D" and estadoCivil != "V" and estadoCivil != "C") or edad <=0 or edad > 100:
    
    if edad < 35 :
        if estadoCivil =="S" or estadoCivil == "D":
            print("Retención del 12%")
        elif estadoCivil == "V" or estadoCivil == "C":
            print("Retención del 11.3%")
    elif edad > 50:
        print("Retención del 8.5%")
    else:
        print("Retención del 10.5%")

else:
    print("los datos son incorrectos")


print ("-------------")

"""8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor”"""

hora1, min1, seg1 = 12, 45, 59
hora2, min2, seg2 = 13, 12, 59

if (0<=hora1<24 and 0<=hora2<24 and 0<=min1<59 and 0<=min2<=59 and 0<=seg1<=59 and 0<=seg2<=59):

    if hora1 < hora2:
        print("La hora 1 es menor que la hora 2")  
    elif hora2 > hora1:
        print("La hora 2 es menor a la hora 1")
    else:
        if min1 < min2:
            print("La hora 1 es menor que la hora 2")
        elif min2 > min1:
            print("La hora 2 es menor a la hora 1")  
        else:
            if seg1 < seg2:
                print("La hora 1 es menor que la hora 2")  
            elif seg1 > seg2:
                print("La hora 1 es menor que la hora 2")
            else:
                print("Las horas coinciden")
 
else:
    print("Los datos son incorrectos")     


print ("-------------")

""""9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se
aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se
aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y
precio original) y calcule el precio rebajado. Debe comprobarse que los
datos de entrada son correctos, y si no lo son mostrar un mensaje de error."""
 
#TIPO A ----> 7%
#TIPO C o <500Euros ----> 12%
#RESTO DE CASOS 9%
 
producto = (input("¿Que tipo de  producto has comprado A, B o C ? "))
precioOriginal = float(input("¿Cuanto vale? "))

if producto == "A" or producto == "a":
    print("Tu producto es de tipo A")
    print("Se aplica un 7% de descuento y el total es", precioOriginal-(precioOriginal*7/100))
elif producto == "B" or producto == "b":
    print("Tu producto es de tipo B")
    print("Se aplica un 9% de descuento y el total es", precioOriginal-(precioOriginal*9/100))
elif producto == "C" or producto == "c":
    print("Tu producto es de tipo C")
    print("Se aplica un 12% de descuento y el total es", precioOriginal-(precioOriginal*12/100))
    if precioOriginal < 500:
        print("Se aplica un 12% de descuento y el total es", precioOriginal-(precioOriginal*12/100))

else:
    print("Los datos son erroneos")
        
print ("-------------")

"""10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error."""

caracter=(input("¿Escribe un caracter?"))
numero1=int(input("¿Escribe un primer numero?"))
numero2=int(input("¿Escribe un segundo numero?"))

if caracter == "/":
    print("Tu caracter es %s " %(caracter))
    print("El rusultado total de la operación es", int(numero1/numero2))
        
elif caracter == "*":
    print("Tu caracter es %s " %(caracter))
    print("El rusultado total de la operación es", int(numero1*numero2))
    
elif caracter == "-":
    print("Tu caracter es %s " %(caracter))
    print("El rusultado total de la operación es", int(numero1-numero2))

elif caracter == "+":
    print("Tu caracter es %s " %(caracter))
    print("El rusultado total de la operación es", int(numero1+numero2))

else:
    print("Error")


print ("-------------")        