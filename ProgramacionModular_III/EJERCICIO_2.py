'''
2. Design a function called lowCaseInString that has a string of characters as parameter,
the method should return how many of those characters are lowercase letters.
'''

cadena= "HoLaQuEEsTAsHaCIendo"


def lowCaseInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i]==cadena[i].lower():
            contador+=1
    return contador

print(lowCaseInString(cadena))