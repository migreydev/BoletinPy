'''
7. Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None.
'''


def isPrime (numero):
    mensaje = True
    for i in range(2, numero):
        if numero%i == 0:
            mensaje = False
    return mensaje

while 1>0:
    numero= int(input("Indica un numero "))
    
    if numero <= 0:
        mensaje = None

    else:
        mensaje= isPrime(numero)
                         
    print(mensaje)
        