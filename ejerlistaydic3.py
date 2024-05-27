#Diccionario de listas: Escribe una función que tome un diccionario donde los valores
#son listas y devuelva una lista que contenga todos los elementos de las listas del
#diccionario.
diccionario={#Creo diccionario con sus dos claves y los valores de cada una en una lista
    "a": ["1","2","3"],
    "b": ["4","5","6"]
    }
def listas(diccionario):#defino la funcion listas
    lista=[]#Creo lista vacia
    for i in diccionario.values():#Itera sobre los valores del diccionario
        lista.extend(i)#agrega todos los valores en una sola lista
    return lista#Devuelve lista
lis=listas(diccionario)#Guardo la funcion
print(lis)#Imprime la nueva lista


    
