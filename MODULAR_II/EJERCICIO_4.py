'''
4. Design a method called getDayOfWeek that receives a list containing three integers
(day, month and year) and returns the day of the week for that date (Monday,
Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).

a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7

'''

def getDayOfWeek(day, month, year):
    a = (14 - month) / 12
    y = year-a
    m = month + 12 * a - 2
    return (((day + y + y/4 - y/100 + y/400 + (31*m)/12)%7))

semana=["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

while 1>0:
    
    day=int(input("Indica un dia "))
    month=int(input("Indica un mes "))
    year=int(input("Indica un año "))
    
    if day <= 0 or month <= 0 or year <= 0:
        mensaje = "Error vuelve a introducir de nuevo los datos"
        
    else:
        mensaje=semana[int(getDayOfWeek(day, month, year))]
            
    print(mensaje)

        