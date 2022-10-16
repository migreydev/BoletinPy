"""9. Design a program that reads an integer positive number greater than 0 and says if
it’s a “perfect number”. A number is perfect if it is equal to the sum of all its divisors.
The messages are the following:
“Enter an integer positive number greater than 0:”
“The number is not valid, try again.”
“The number is perfect.”
“The number is not perfect."""

#Diseñe un programa que lea un número entero positivo mayor que 0 y diga si es un numero perfecto
#Un número es perfecto si es igual a la suma de todos sus divisores.

numero = int(input("Ingrese un numero mayor al 0 "))
sumaDivisores=0

while numero < 1:
    numero = int(input("No es correcto. Ingrese un numero mayor al 0 "))
    
for i in range(1,(numero//2)+1):
    print(i)
    if numero%i==0:
        sumaDivisores+=i
        
# la i son todos los divisores
        
if  sumaDivisores == numero:
    print("El numero %s es perfecto" %(numero))
else:
    print("El numero %s no es perfecto " %(numero))