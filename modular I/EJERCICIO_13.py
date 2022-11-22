'''13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.'''


nombres=["Manuel", "Daniel", "Ismael", "Ana", "Alvaro", "Cristina", "Alejandro"]
lista=[]

def obtenerNombre(nombres):
    for i in nombres:
        if i[0]=='A':
            lista.append(i)

    return lista

print(obtenerNombre(nombres))
        
