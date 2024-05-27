#Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
#elementos en orden inverso.
lista=[2,3,4,5,6,7,8,9,45,56,76]#Creo la lista con los valores
def invertir_lista(lista):#Defino la funcion de invertir lista
    return lista[::-1]#Devuelve la lista invertida usando el segmento corte extendido donde los primeros ":"son el indicie de incio los segundos ":"el indice de fin 
resultado=invertir_lista(lista)#Guardo la funcion 
print(lista)#Imprimo la lista normal
print(f"La lista invertida: {resultado}")#Imprimo la lista invertida

