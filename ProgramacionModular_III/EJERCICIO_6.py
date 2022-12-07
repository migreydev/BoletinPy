'''
6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo,
si la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False. Las letras
de la palabra escondida deben aparecer en el orden correcto en la cadena que la oculta:
shybaoxlna ⇒ hola: True
soybahxlna ⇒ hola: False
'''

palabra="shybaoxlna"
buscar = "hola"

def obtenerPalabra(buscar, palabra):
    mensaje = False
    contador=0
    for i in palabra:
        for letra in buscar:
            if i == letra:
                contador+=1
                mensaje = True 
    return mensaje

print(obtenerPalabra(buscar, palabra))


    