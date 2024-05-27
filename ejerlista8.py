#Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
#que sea la concatenación de ambas.
lista1=[1,2,3,4,5]#Creo la primera lista con sus valores
lista2=[6,7,8,9,10]#Creo la segunda lista con sus valores
def concatenar(lista1,lista2):#Defino la funcion concatenar con los argumentos lista1, lista2
    lista3=lista1+lista2#Creo la lista3 y sume los valores de la primera lista con la segunda
    return lista3#Devuelve lista3
juntar_listas=concatenar(lista1,lista2)#Guardo la funcion 
print(juntar_listas)#Imprime las dos listas concatenadas