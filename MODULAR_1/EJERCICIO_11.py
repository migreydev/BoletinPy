'''11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno.'''

lista1=[1,3,4,5,6,9,8]

lista2=[1,5,7,5,1,9,1]

listaComun=[]

def obtenerComunes(lista1, lista2):
    if len(lista1)>len(lista2):
        for i in range(len(lista1)):
            if lista1[i]==lista2[i]:
                listaComun.append(lista1[i])
            
    else:
        for i in range(len(lista2)):
            if lista1[i]==lista2[i]:
                listaComun.append(lista2[i])
                
    return listaComun

print(obtenerComunes(lista1, lista2))
    
    