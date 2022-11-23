"""K"3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo."""

dd, mm, yyyy = 1, 1, 2022
def es_bisiesto (year):
    bisiesto = year % 4 == 0 and (year % 100 != 0 or year % 4 == 0)
    return (bisiesto)
def transformar_formato_largo (dd, mm, yyyy):
    
    nombre_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    dias_maximo_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    
    if 1 <= mm <= 12 and((1<= dd <= dias_maximo_meses[mm-1]) or (es_bisiesto (yyyy) and 1<= dd <= 29 and mm == 2)):
        
        mensaje = f'{dd} de {nombre_meses[mm-1]} de {yyyy}'
    
    else:
        mensaje = "La fecha introducida no es válida."
    
    return mensaje
day = int(input("Introduce el día:"))
month = int(input("Introduce el mes:"))
year = int(input("Introduce el año:"))
while day >= 0:
    print(transformar_formato_largo(day, month, year))
    
    day = int(input("Introduce el día:"))
    month = int(input("Introduce el mes:"))
    year = int(input("Introduce el año:"))