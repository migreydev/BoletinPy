'''
10. Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa.
'''


def isFriendNumber(a, b):
    suma=0
    for i in range(1,numeroA):
        if numeroA%i==0:
            suma+=i

    return suma==numeroB

while 1>0:
    
    numeroA=int(input("Indique un numero "))
    numeroB=int(input("Indique otro número "))
    
    if numeroA <= 0 and numeroB <= 0:
        mensaje = "El numero introducido no es correcto "
    
    else:
        mensaje = isFriendNumber(numeroA, numeroB)
        
        print(mensaje)
        
