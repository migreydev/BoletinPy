"""7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]"""
#[0,1] [0,1]


ficha1 = [3,5]
ficha2 = [2,2]

def encajan(ficha1, ficha2):
    compatibilidad="No encaja"
    if (ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1]) or (ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]):
            compatibilidad = "Encaja"
    return compatibilidad

print(str(ficha1) + str((ficha2)))       
print(encajan(ficha1, ficha2))