'''
3. Design a function called upperCaseInString that has a string of characters as parameter
and the method should return how many are uppercase letters
'''

cadena= "Holaaa queeEe Estass HAciEndO"

def upperCaseInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i]==cadena[i].upper():
            contador+=1
    return  contador

print(upperCaseInString(cadena))
