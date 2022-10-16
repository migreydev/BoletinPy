""" 1. Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages. """

#MOSTRAR TODOS LOS NUMEROS ENTRE 1-100
#SI EL NUMERO ES MULTIPLO DE 7 DEBE APARECER UN MENSAJE 
#SI ES MULTIPLO DE 13 DEBE MOSTRAR UN MENSAJE
#SI ES MULTIPLO DE 7 Y 13 DEBE APARECER UN MENSAJE 

numero = 0


for numero in range(0,101):
    print(numero)
    if numero%7==0:
        print("El numero %s es un multiplo de 7" %(numero))
        if numero%7==0 and numero%13==0:
            print("El numero %s es multiplo de 7 y de 13" %(numero))
        
    elif numero%13==0:
        print("El numero %s es un multiplo de 13" %(numero))
        
        if numero%7==0 and numero%13==0:
            print("El numero %s es multiplo de 7 y de 13" %(numero))
            
else:
    print("Fin")
    