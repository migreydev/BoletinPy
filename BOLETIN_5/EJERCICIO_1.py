"""1. Escribe el código de un programa que reciba un número de nota de 0 a 100 y nos
informe de las calificaciones en el siguiente formato:"""

#90-100, Sobresaliente
#70-89, Notable
#60-69, Bien
#50-59, Suficiente
#0-49, Suspenso

nota=int(input("Escribe un número de 0 al 100 para indicar una nota "))

if nota>=90 and nota <=100:
    print(f"Tu nota es de {nota} ¡Sobresaliente!")

elif nota >=70 and nota <=89:
    print(f"Tu nota es de {nota} ¡Notable!")

elif nota >=60 and nota <=69:
    print(f"Tu nota es de {nota} ¡Bien!") 

elif nota >=50 and nota <=59:
    print(f"Tu nota es de {nota} ¡Suficiente!")

else:
    print(f"Tu nota es de {nota} ¡Suspenso!")