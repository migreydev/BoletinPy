'''
14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .
'''
cadena1= "hola", "papa", "que", "haces"
cadena2= "holaaa", "papaa", "que", "estas", "haciendo"
cadena3= "holaa", "papaa", "quee", "haces"

def obtenerCadena(cadena1, cadena2, cadena3):
    x=0
    while x < len(cadena1) and  x < len(cadena2) and x < len(cadena3):
        if len(cadena1) < len(cadena2) > len(cadena3):
            print(f"{cadena2} cadena2 es más grande")
        elif len(cadena2) < len(cadena1) > len(cadena3):
            print(f"{cadena1} cadena1 es más grande")
        else:
            print(f"{cadena3} cadena3 es más grande")
        x+=1

print(obtenerCadena(cadena1, cadena2, cadena3))