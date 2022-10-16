#TEMA 1 INTRODUCCION A LA PROGRAMACIÓN

#1. Calcular el resultado de las siguientes expresiones lógicas
print(7>=27 and not(7<=2))
#FALSE

print(24>5 and 10<=10 or 10==5)
#TRUE

print(10>=15 or 23==13) and not (8==8) 
#FALSE

print(not(6/3>3) or 7>7)
#TRUE

print("-----")

# 2.Calcular el valor de las siguientes expresiones aritméticas
#a) 27 mod 4 + 15\4
print(27%4 + 15/4, type(27%4 + 15/4))
#RESULTADO 6,75

# b) 37\4^2–2
print(37/4**2-2, type(37/4**2-2))
#RESULTADO 0.3125

# c) 9*2/3*10*3
print(9*2/3*10*3, type(9*2/3*10*3))
#RESULTADO 180

# d) (7*3–4*4)^2\4*2
print((7*3-4*4)**2/4*2, type((7*3-4*4)**2/4*2))
#RESULTADO 12.5

print("-----")


#3. Escribir una expresión lógica que cumpla:
#a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60 euros pero igual o inferior a 420 euros.

#FALSE
precio=0
print(60 <= precio and precio <= 420)
precio=500
print(60 <= precio and precio <= 420)

#TRUE
precio = 60
print(60 <= precio and precio <= 420)
precio=400
print(60 <= precio and precio <= 420)
precio=420
print(60 <= precio and precio <= 420)

# b)Debe ser Verdadera si el numero contenido en la variable entera numero es impar.

numero=17
print(numero%2==1)

#c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son válidas

#TRUE
saldo=500; dineroSacar=250

print(saldo >=0 and saldo >= dineroSacar and dineroSacar>0)


#d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que estén comprendidas entre 0:0 y 23:59
hora=23; minutos=59

print(hora >=0 and hora <= 23 and minutos >=0 and minutos <=59)

#e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado)

estadoCivil = 'S'
print (not(estadoCivil == 'S' or estadoCivil == 'C' or  estadoCivil == 'V' or estadoCivil == 'D')) #False
print ((estadoCivil != 'S' or estadoCivil != 'C' or  estadoCivil != 'V' or estadoCivil != 'D')) #True

print("-----")

#4. Escribir una expresión lógica que cumpla:

#a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero es superior a 300 euros o negativa.

cantidad= -1
cantidad = 0
cantidad = 200
cantidad = 300

print(0 < cantidad <=300) #True
print(not(0 < cantidad <=300))#False

#b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22 años.
edad = 18 #False
print(not((16 < edad < 22)))
edad = 14 #True
print(16 > edad < 22)

#c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida
repuesta='S'
respuesta='N'
print(not((respuesta != 'S' or respuesta !='N'))) #False

#d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
numero = 21 # false
print(not(numero%7 ==0 or numero%3==0))
numero = 16 # true
print(not(numero%7 ==0 or numero%3==0))


print("-----")

#5. Escribir la tabla de verdad para las siguientes expresiones lógicas

# a) (A OR B) AND NOT(A)

a,b= True, True
print((a or b) and not (a)) #FALSE
a,b =True, False
print((a or b) and not (a)) #FALSE
a,b =False, True
print((a or b) and not (a)) #TRUE
a,b =False, False
print((a or b) and not (a)) #FALSE


#b) NOT (A OR B) AND B
a,b= True, True
print(not(a or b) and b) #FALSE
a,b =True, False
print(not(a or b) and b) #FALSE
a,b =False, True
print(not(a or b) and b) #FALSE
a,b =False, False
print(not(a or b) and b) #FALSE


#c) A OR NOT (B)
a,b= True, True
print(a or not b) #TRUE
a,b =True, False
print(a or not b) #TRUE
a,b =False, True
print(a or not b) #FALSE
a,b =False, False
print(a or not b) #TRUE


#d) NOT ((A AND B) AND (B OR A))
a,b= True, True
print(not((a and b) and (b or a))) #FALSE
a,b =True, False
print(not((a and b) and (b or a))) #TRUE
a,b =False, True
print(not((a and b) and (b or a))) #TRUE
a,b =False, False
print(not((a and b) and (b or a))) #TRUE

