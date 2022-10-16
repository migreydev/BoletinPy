"""2. Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format:
7*0=0
7*1=7
…..
7*10=70"""

#DISEÑA UN PROGRAMA QUE LEA UN NUMERO ENTERO ENTRE 0 Y 10 Y MUESTRE LA TABLA DE MULTIPLICAR 
#SI EL NUMERO SE ENCUENTRA FUERA INGRESE UN MENSAJE QUE INDIQUE "EL NUMERO ESTA FUERA DE LOS LIMITES 


numero=int(input("Ingrese un número entre 0 y 10 "))


for i in range(0,11):
    multiplicacion = i*numero
    print(multiplicacion)
if numero>0 and numero<10:
    print("El numero se encuentra en los limites")
else:
    print("El numero se encunetra fuera de los limites")
     
