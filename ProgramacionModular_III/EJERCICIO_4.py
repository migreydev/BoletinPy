'''
4. Design a function called numberInString that receives a string of characters as
parameter and returns how many of them are numbers
'''

cadena= "45667432H"

def numberInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i] in "1234567890":
            contador+=1
    return contador

print(numberInString(cadena))
            
    
        