"""10. Design a program that reads an integer positive number and says the “factorial” of
the number. To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try again.”
“The factorial is XX"""

#Diseña un programa que lea un numero entero positivo y diga "factorial de el numero". 

#FACT(0)= 1 
#FACT (1)= 1
#FACT (2)=2
#FACT (3)=6
#FACT (4)=24


numero = int(input("Indique un número positivo "))
total = 1

for i in range(1, numero+1):
    print(i)
    total*=i
print(total)


while numero > 0:
    total *=numero
    numero-=1
print(total)
