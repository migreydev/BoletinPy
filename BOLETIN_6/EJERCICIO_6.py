"""6. Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
Enter one number:
The product is XX"""


#Diseñe un programa que lea dos números enteros, por ejemplo númeroA y númeroB
#calcula el producto de ambos números sin usar la multiplicación, pero utilizando la suma.

numeroA=int(input("Ingrese un número "))
numeroB=int(input("Ingrese otro número "))
total = 0

for i in range(1,numeroB+1,1):
    total = total+numeroA
print("El producto es %s" %(total))