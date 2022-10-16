"""2. Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio
(Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio)."""

#Fecha actual (día y mes) y el hemisferio (Norte/Sur) e indique en qué estación se encuentra:


#HEMISFERIOR N  --> OTOÑO 23 SEPTIEMBRE A 21 DICIEMBRE, INVIERNO DEL 21 DICIEMBRE A 21 DE MARZO, PRIMAVERA 21 MARZO A 21 JUNIO Y VERANO 21 JUNIO A 23 SEPTIEMBRE
#HEMISFERIOR S -->  PRIMAVERA 23 A 21 DE DICIEMBRE, VERANO DEL 21 DICIEMBRE A 21 MARZO, OTOÑO 21 DE MARZO A 21 JUNIO Y INVIERNOS 21 JUNIO  A 21 SPETIEMBRE

dia=int(input("Indique un día "))
mes=input("Indique un mes ")
hemisferio=input("Indique el hemisferio N/S ")

if hemisferio=="N":
    if (dia>=23 or dia<=21) and (mes=="Septiembre" or mes=="Octubre" or mes=="Noviembre" or mes=="Diciembre"):
        print("La estacion es Otoño")
    elif (dia>=21 or dia<=21) and (mes=="Diciembre" or mes=="Enero" or mes=="Febrero" or mes=="Marzo"):
        print("La estacion es Invierno")
    elif (dia>=21 or dia<=21) and (mes=="Marzo" or mes=="Abril" or mes=="Mayo" or mes=="Junio"):
        print("La estacion es Primavera")
    elif (dia>=21 or dia<=21) and (mes=="Junio" or mes=="Julio" or mes=="Agosto" or mes=="Septiembre"):
        print("La estacion es Verano")
        
elif hemisferio=="S" :
    if (dia>=23 or dia<=21) and (mes=="Septiembre" or mes=="Octubre" or mes=="Noviembre" or mes=="Diciembre"):
        print("La estacion es Primavera")
    elif (dia>=21 or dia<=21) and (mes=="Diciembre" or mes=="Enero" or mes=="Febrero" or mes=="Marzo"):
        print("La estacion es Verano")
    elif (dia>=21 or dia<=21) and (mes=="Marzo" or mes=="Abril" or mes=="Mayo" or mes=="Junio"):
        print("La estacion es Otoño")
    elif (dia>=21 or dia<=21) and (mes=="Junio" or mes=="Julio" or mes=="Agosto" or mes=="Septiembre"):
        print("La estacion es Invierno")   
    
else:
    print("Datos incorrectos")
        
