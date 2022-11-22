'''12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).'''

from random import randint

lista1=[]
lista2=[]
listaUnion=[]

for i in range(5):
    lista1.append(randint(0,7))


for i in range(5):
    lista2.append(randint(0,7))
    
    
def unionListas(lista1, lista2):
    for i in lista1:
        if i not in lista2:
            listaUnion.append(i)
    return listaUnion
      
print(lista1)
print(lista2)
print(unionListas(lista1, lista2))

