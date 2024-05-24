#Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
#sin elementos duplicados.
lista=[1,1,1,2,2,3,4,4,5,6,7,8,8,8,8,9,9,9]#Creo la lista con sus valores
def Eliminar_duplicados(lista):#Creo la funcion  eliminar duplicados
    return list(set(lista))#Convierte la lista en un conjunto de elementos unicos
lista_nueva=Eliminar_duplicados(lista)#Guardo la funcion en lista nueva
print("Se Eliminaron los duplicados")#Imprime mensaje
print(lista_nueva)#Imprime la lista nueva

          