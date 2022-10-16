""""4. Design a program that reads a positive number N greater than 0 and show the result
of the sum of the N numbers between 1 and N. If the number N is not valid, the
program should ask for it again. The messages are the following:
“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX.”"""

#Diseña un programa que lea un número positivo mayor que 0 y muestre el resultado de la suma de los números entre 1 y N.
#Si el número N no es válido, el programa debería volver a pedirlo.

valor=0

n=int(input("Ingrese un número mayor al 0 "))


while n <=0:
    n=int(input("No es valido, ingrese de nuevo un número mayor a 0 "))
    if n> 0:
        print("Es correcto")
for i in range(1, n+1):
    print(i)
    valor=valor+i
print("La suma de N es %s" %(valor))