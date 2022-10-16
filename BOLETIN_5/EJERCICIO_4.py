"""4. Existen cuatro grupos sanguíneos en seres humanos, que se multiplican por dos si
consideramos el factor Rh. Unos grupos son compatibles con otros atendiendo al
criterio que podemos ver en las siguientes tablas."""

#Elabora un programa que reciba dos grupos sanguíneos y devuelva si son compatibles y en qué sentido

grupo1=input("Indique un grupo sanguineo ((A), (B), (AB) y (0) +-) " )
grupo2=input("Indique un grupo sanguineo ((A), (B), (AB) y (0) +-) " )

if (grupo1 == "0-" and grupo2 == "0-"): 
    print("Son compatibles")
elif (grupo1 == "0+" and grupo2 == "0-") or (grupo1 == "0+" and grupo2 == "0+"):
    print("Son compatibles")
elif (grupo1 == "A-" and grupo2 == "0-") or (grupo1 == "A-" and grupo2 == "A-"):
    print("Son compatibles")
elif (grupo1 == "A+" and grupo2 == "0-") or (grupo1 == "A+" and grupo2 == "0+") or (grupo1 == "A+" and grupo2 == "A-") or (grupo1 == "A+" and grupo2 == "A+"):
    print("Son compatibles")
elif (grupo1 == "B-" and grupo2 == "0-") or (grupo1 == "B-" and grupo2 == "B-"):
    print("Son compatibles")
elif (grupo1 == "B+" and grupo2 == "0-") or (grupo1 == "B+" and grupo2 == "0+") or (grupo1 == "B+" and grupo2 == "B-") or (grupo1 == "B+" and grupo2 == "B+"):
    print("Son compatibles")
elif (grupo1 == "AB-" and grupo2 == "0-") or (grupo1 == "AB-" and grupo2 == "A-") or (grupo1 == "AB-" and grupo2 == "B-") or (grupo1 == "AB-" and grupo2 == "AB-"):
    print("Son compatibles")
elif (grupo1 == "AB+" and grupo2 == "0-") or (grupo1 == "AB+" and grupo2 == "0+") or (grupo1 == "AB+" and grupo2 == "A-") or (grupo1 == "AB+" and grupo2 == "A+") or (grupo1 == "AB+" and grupo2 == "B-") or (grupo1 == "AB+" and grupo2 == "B+") or (grupo1 == "AB+" and grupo2 == "AB-") or (grupo1 == "AB+" and grupo2 == "AB+"):
    print("Son compatibles")
else:
    print("No son compatibles")   
        
        
        
        
        
        
        
        
        
        