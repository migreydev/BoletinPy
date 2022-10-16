"""8. Design a program that asks for a set of numbers. After inputting each number, the
program should ask “Do you want to enter more numbers (Y/N)?”. If the answer is “Y”
the program asks for other numbers. When the user finishes to enter all the numbers,
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”"""

#Diseñe un programa que solicite un conjunto de números
#Después de ingresar cada número, el programa debe preguntar "¿Desea ingresar más números (S/N)?". Si la respuesta es "S" el programa pide otros números.
#Cuando el usuario termine de ingresar todos los números, el programa debe decir cuál es el más pequeño. Los mensajes son los siguientes:


numero = int(input("Introduce un numero "))
pequeno = numero 

pregunta = input("¿Deseas ingresar más numeros (S/N)? ")

while pregunta.upper()=="S":
    if numero < pequeno:
        pequeno = numero
    numero = int(input("Introduce un numero"))  
    pregunta = input("¿Deseas ingresar más numeros (S/N)? ")


print("El numero más pequeño es %s " %(pequeno))