#Escribir una expresión lógica que cumpla:
"""a) Debe ser Verdadera si el contenido de las variables enteras sueldo_bruto y sueldo_neto es
el adecuado para una retención del 22%."""
sueldo_bruto = 2000
sueldo_neto =1560

print(sueldo_bruto-sueldo_bruto*22/100==sueldo_neto) #TRUE


"""b) Debe ser Verdadera si el contenido de la variable entera día es un valor válido para el mes
de mayo"""

dia= -1
valido= dia >=1 and dia <=31
valido2= dia >0 and dia <32
valido3= 1 <= dia <= 31

dia= 1
valido= dia >=1 and dia <=31
valido2= dia >0 and dia <32
valido3= 1 <= dia <= 31

dia=2
valido= dia >=1 and dia <=31
valido2= dia >0 and dia <32
valido3= 1 <= dia <= 31

dia=31
valido= dia >=1 and dia <=31
valido2= dia >0 and dia <32
valido3= 1 <= dia <= 31

dia=32
valido= dia >=1 and dia <=31
valido2= dia >0 and dia <32
valido3= 1 <= dia <= 31
print(valido, valido2, valido3)


"""c) Debe ser Verdadera si el número contenido en las variables enteras num1 y num2 son
múltiplos de tres."""
num1 =21 
num2 = 12
print(num1%3 ==0 and num2%3 ==0) #TRUE

"""d) Debe ser Verdadera si la calificación contenida en la variable real nota es un aprobado."""
nota=5
print(nota >=5 and nota<=10)#TRUE

nota=3
print(nota >=5 and nota<=10)#FALSE

"""e) Debe ser Verdadera si la media de la calificación contenida en las variables reales nota1,
nota2 y nota3 es un aproblado"""

nota1=6
nota2=4
nota3=8
notaMedia=(nota1+nota2+nota3)/3
print("La nota media es de", ((nota1+nota2+nota3)/3)) 
print(notaMedia >=5 and notaMedia<=10)

print("-----")

#Escribir una expresión lógica que cumpla:
"""a) Debe ser Falsa si alguna de las calificaciones contenidas en las variables reales nota1, nota2
y nota3 es un suspenso."""

nota1=5
nota2=3
nota3=5
print(nota1 >=5 and nota2 >=5 and nota3 >=5) #FALSE

"""b) Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga menos de
1000 euros en la variable saldo o se haya quedado al descubierto más de 5 veces. Este
último dato se almacenará en la variable descubierto"""

saldo=1000
descubierto=5

print(saldo >=1000 and descubierto <5)#FALSE

""""c) Debe ser Falsa cuando el valor almacenado en la variable asignaturasAprobadas sea
inferior al 30% del valor almacenado en la variable asignaturasCurso."""

asignaturasAprobadas=3
asignaturasCurso=10

print(asignaturasCurso-asignaturasCurso*30/100 == asignaturasAprobadas)#FALSE


""""d) Debe ser Falsa si los números contenido en las variables enteras mes y día no son válidos.
Vamos a considerar que no hay años bisiestos."""

#TRUE
mes = 2
dia = 25

mesValido = ((mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30)) or ((mes==2) and (1<=dia<=28)) or ((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12))

print(mesValido)

#FALSE
mes = 2
dia = 30

mesValido = ((mes==4 or mes==6 or mes==9 or mes==11) and (1<=dia<=30)) or ((mes==2) and (1<=dia<=28)) or ((mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12))

print(mesValido)
