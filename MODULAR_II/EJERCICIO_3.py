'''
3. Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1.
'''

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def isLeapYear(agno):
    return agno%4==0 and (agno%100!=0 or agno%400==0)


def computeDaysInMonth (meses, agno):
    dias_maximo=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
    if meses==2 and  isLeapYear(agno):
        dias_maximo=29
        
    else:
        dias_maximo=dias_maximo[meses-1]
    
    return dias_maximo


while 1>0:
    month=int(input("Indica un mes (Referente al número 1-12): "))
    
    agno=int(input("Indica un año: "))
    
    if month<=0 or agno<=0:
        mensaje=-1
    else:
        mensaje=f"{meses[month-1]} de {agno}, tiene {computeDaysInMonth(month, agno)} dias"
            
    print(mensaje)

    
    

