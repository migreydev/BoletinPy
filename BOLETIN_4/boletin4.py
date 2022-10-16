"""1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
#c=(a**2+b**2)

import math 
a=float(input("ingrese un cateto "))
b=float(input("ingrese el otro cateto "))
c=math.sqrt(a*a+b*b)
print(c)

print("---------------")

"""2.Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""

f = int(input("Escribe un valor en grados Fahrenheit "))

c = (f-32)*5/9
print(c,"°C")  

print("---------------")

""""3. Calcular la media de tres números pedidos por teclado"""

numero1=int(input("Escribe un primer número "))
numero2=int(input("Escribe un segundo número "))
numero3=int(input("Escribe un tercer número "))

print("La media es ", (numero1 + numero2 + numero3)/3)

print("---------------")

"""4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra."""
            
compra=int(input("¿Cuanto es el total de la compra? "))
descuento=((compra)-(compra*15)/100)

if descuento:
    print("El total de su compra, junto al descuento es de %s euros" %(descuento))
    
""""5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""

from math import sqrt

x1=float(input("Escribe x1"))
y1=float(input("Escribe y1"))

x2=float(input("Escribe x2"))
y2=float(input("Escribe y2"))
distancia=sqrt((x2-x1)**2 + (y2-y1)**2)
print("La distancia entre dos puntos es %s" %(distancia))

print("---------------")

"""6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos"""

from math import sqrt

x1 = float(input("Escribe x1 "))
y1 = float(input("Escribe y1 "))
x2 = float(input("Escribe x2 "))
y2 = float(input("Escribe y2 "))

d = sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print("La distancia entre dos puntos es: %s" %(d))


print("---------------")

""""7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?"""

from math import sqrt

n=(float(input("Escribe un numero")))

r2=sqrt(n)
r3=n**(1/3)

print("La raiz cuadrada es: %s" %(r2), "y la raiz cubica es: %s" %(r3))

print("---------------")


""""8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos)."""


dosEuros=int(input("¿Cuantas monedas de dos euros tienes?"))
unEuros=int(input("¿Cuantas monedas de un euro tienes?"))
cincuentaCentimos=int(input("¿Cuantas monedas de cincuenta centimos tienes?"))
veinteCentimos=int(input("¿Cuantas monedas de veinte centimos tienes?"))
diezCentimos=int(input("¿Cuantas monedas de un diez centimos tienes?"))

total= dosEuros * 200 + unEuros * 100 + cincuentaCentimos *50 + veinteCentimos *20 + diezCentimos *10;
euros= int(total/100);
centimos = total % 100;

print("Tenemos %s euros" %(euros), "y %s centimos" %(centimos))


print("---------------")


"""9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

 
base = float(input("Escribe la base "))
exponente= float(input("Escribe el exponente "))
potencia= (base**exponente);


if exponente >= 0:
    print("El resultado es ", potencia)

elif exponente == 0:
    print("El resultado es ", 1/ potencia)

else:
    print ('El resultado es : ',(1/potencia(exponente)))
    
    
print("---------------")

"""10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno."""

base=float(input("Escriba la base "))
altura=float(input("Escriba la altura "))
area=float(input("Escriba el area "))

if  base< area:
    print("Es un triangulo rectángulo")

elif base < altura:
    print("Es un triangulo isósceles")
    
elif base == altura:
    print("Es un triangulo equilátero")
    
else:
    print("Es un triagunlo escaleno")


print("---------------")

"""11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400""" 


ano= int(input("Escribe un año "))

if ano%4 == 0:
    print(("El %s es bisiesto ") %(ano))
 
elif ano%100 !=0:
    print(("El %s no es bisiesto") %(ano))
 
else:
    print(("El %s no es bisiesto") %(ano))  


print("---------------")


"""12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida"""

tipo= str(input("Indique el tipo de uva "))
tamano= int(input("Indique el tamaño de uva "))
precio = float(input("¿Cual es el precio? "))

"""SE LE CARGAN 20 CENT CUANDO ES TAMAÑO 1 y 30 CENT CUANDO ES TAMAÑO 2 SE REBAJAN 30 CENT 
CUANDO ES TAMAÑO 1 Y 50 CENT CUANDO ES TAMAÑO 2"""


if tipo == "a":
    print(("El tipo de uva es %s ") %(tipo))
    if tamano == 1:
        print(("El tamaño de la uva es %s ") %(tamano))
        if (precio+0.20):
            print("El total es", precio+0.20)
    
    elif tamano == 2:
        print(("El tamaño de la uva es %s ") %(tamano))
        if (precio+0.30):
            print("El total es", precio+0.30)

elif tipo == "b":
    print(("El tipo de uva es %s ") %(tipo))
    if tamano == 1:
        print(("El tamaño de la uva es %s ") %(tamano))
        if (precio-0.30):
            print("El total es", precio-0.30)

    elif tamano == 2:
        print(("El tamaño de la uva es %s ") %(tamano))
        if (precio-0.50):
            print("El total es", precio-0.50)

else:
    print("Error")
    
    
    
print("---------------")

"""13. El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje"""


#100 o mas alumnos el coste por cada alumno es 65 euros
#50 a 99 alumnos el coste es de 70 euros
#30 a 49 el coste es de 95 euros
#Menos de 30 el coste es de 4000

nAlumnos =int(input("¿Cuantos alumnos son?"))
totalAlum = 0 

if nAlumnos >= 100:
    print("El pago total a la agencia es de", nAlumnos*65, "cada alumno debe de pagar 65 euros")

elif nAlumnos > 50 and nAlumnos < 99:
        print("El pago total a la agencia es de", nAlumnos*70, "cada alumno debe de pagar 70 euros")
elif nAlumnos > 30 and nAlumnos < 49:
        print("El pago total a la agencia es de", nAlumnos*95, "cada alumno debe de pagar 95 euros")
   
else:
    print("El coste del autobus es de 4000 euros y cada alumno debe pagar", (4000/nAlumnos), "euros")


print("---------------")


"""14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada."""



print("---------------")


"""15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error."""

dia = int(input("Escribe número para indicar el día de la semana "))

if dia == 1:
    print("El día de la semana es Lunes")

elif dia == 2:
    print("El día de la semana es Martes")

elif dia == 3:
    print("El día de la semana es Miercoles")
    
elif dia == 4:
    print("El día de la semana es Jueves")
    
elif dia == 5:
    print("El día de la semana es Viernes")
    
elif dia == 6:
    print("El día de la semana es Sabado")
    
elif dia == 7:
    print("El día de la semana es Domingo")

else:
    print("Error")
    
print("---------------")

"""16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente."""


numero = int(input("Escribe un número entero entre uno y doce "))

if numero == 1:
    print("El mes de enero tiene 31 días")

elif numero == 2:
    print("El mes de febrero tiene 28 días")

elif numero == 3:
    print("El mes de marzo tiene 31 días")
    
elif numero == 4:
    print("El mes de abril tiene 30 días")
    
elif numero == 5:
    print("El mes de mayo tiene 31 días")
    
elif numero == 6:
    print("El mes de junio tiene 30 días")
    
elif numero == 7:
    print("El mes de julio tiene 31 días")
    
elif numero == 8:
    print("El mes de agosto tiene 31 días")
    
elif numero == 9:
    print("El mes de septiembre tiene 30 días")
    
elif numero == 10:
    print("El mes de octubre tiene 31 días")
    
elif numero == 11:
    print("El mes de noviembre tiene 30 días")
    
elif numero == 12:
    print("El mes de diciembre tiene 31 días")

else:
    print("Error")

    
print("---------------")