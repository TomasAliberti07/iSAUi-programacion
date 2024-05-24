#Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.
lista=[1,1,1,1,1,2,2,2,3,3,4,4,5,6,6,7,8,9,9,9]#Creo una lista con sus valores
print(lista)#Imprime la lista para que vea el usuario
def contar_valor(lista):#Creo la funcion contar valor con el argumento lista
    valor=int(input("Introduce un valor que aparezca en la lista:"))#Le pido al usuario que ingrese el valor
    return lista.count(valor)#Devuelve la cantidad de veces que se repite un valor en la lista con la funcion count
valores=contar_valor(lista)#Guardo la funcion
print(f"Se repite: {valores}")#Imprime la cantidad de veces que se repite el valor