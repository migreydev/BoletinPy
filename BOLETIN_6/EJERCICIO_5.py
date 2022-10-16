""""5. Design a program that asks for numbers until the user inputs a negative one. When
this happens, the program will show how many positive numbers have been
introduced by the user. The messages are the following:
“Enter a number (negative to finish):”
“You have entered XX positive numbers.”"""

suma=0
contador=0

n=int(input("Ingresa un número (ingresa uno negativo para terminar) "))
while n >= 0:
    n=int(input("Ingresa un número (ingresa uno negativo para terminar) "))
    suma+=n
    contador+=1
    if n <=0:
        print(f"Has ingresado {contador} numeros positivos")
        

        