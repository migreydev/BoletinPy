'''
1. Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None.
'''
numero = int(input("Indique un número "))
factorial = 1

def obtenerFactorial(numero):
    while 0 < numero:
        factorial=1
        for i in range(1, numero+1):
            factorial= factorial * i
        return factorial
    return None
print(obtenerFactorial(numero))       
            
