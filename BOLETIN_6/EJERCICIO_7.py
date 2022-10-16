"""7. Design a program that asks how many numbers the user wants to write. After the
user enters all numbers, the program should say the medium of the numbers. If the
user inputs a wrong number, the program should ask for it again. The messages are
the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The medium is XX.XX” to show the result"""

#Diseñe un programa que pregunte cuántos números desea escribir el usuario.
#Después de usuario ingresa todos los números, el programa debe decir el medio de los números.
#Si el usuario ingresa un número incorrecto, el programa debería solicitarlo nuevamente.

valor = 0
numeros = int(input("¿Cuántos números deseas introducir? "))
while True:
    if numeros <= 0:
        print("Número no valido, ingrese un nuevo numero superior a 0")
    else:
        print("Numero correcto")
    for x in range(numeros):
        valor += int(input("Ingrese un número mayor a 0 "))
    print("Se han introducido", numeros, "números y la media de estos números es", valor/numeros)