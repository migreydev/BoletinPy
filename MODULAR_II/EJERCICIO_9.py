'''
9. Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None.
'''


def getPrimeDivisors(numero):
    listaDivisor=[]
    for i in range(1,numero+1):
        sumar=0
        for elemento in range(1,i+1):
            if i%elemento==0:
                sumar+=1
        if sumar==2:
            listaDivisor.append(i)
    return listaDivisor


while 1>0:
    numero= int(input("Indica un numero "))
    
    if numero <= 0:
        mensaje = None

    else:
        mensaje=getPrimeDivisors(numero)
                         
    print(mensaje)

    
