"""3. Design a program that asks how many numbers the user wants to introduce. Then,
the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative
number, it is not valid, and the system should ask for another number. The messages
are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The number XX is odd”
“The number XX is even”"""

#Diseña un programa que pregunte cuántos números quiere introducir el usuario
#El usuario tendría que introducir los números uno a uno y el programa debería decir si cada uno de los números es par o impar.
#Si el usuario ingresa 0 o un negativo, no es válido, y el sistema debe pedir otro número.

cantidad = int(input("Ingrese un numero mayor al 0 "))


while cantidad <= 0:
    cantidad = int(input("No es correcto. Ingrese un numero mayor al 0 "))
    
for i in range(cantidad):
    numero = int(input("Ingrese un numero mayor al 0 "))
    
    while numero <=0:
        numero= int(input("No es correcto. Ingrese un numero mayor al 0 "))
    
    if numero%2==0:
        print("Es par")
    elif numero%2!=0:
        print("Es impar")

        