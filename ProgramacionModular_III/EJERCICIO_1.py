'''
1. Design a function called charactersInString that has a character string and a character
as input parameters and returns how many times that character appears in the string. It
should do it no matter if the string and character are lower case or upper case characters.
'''

cadena="HOLAA QUE ESTAS HACIENDO".upper()
letra="E".upper()



def charactersInString(cadena, letra):
    contador=0
    for i in range(len(cadena)):
        if cadena[i]==letra:
            contador+=1
    return contador

print(charactersInString(cadena, letra))