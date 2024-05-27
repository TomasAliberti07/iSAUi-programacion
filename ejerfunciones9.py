#Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
#lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.
def ordenar_lista(lista):#Defino la funcion ordenar lista con el argumento lista
    ordenar=sorted(lista)#La funcion sorted va ordenar cada palabra que esta dentro de la variable ordenar
    return ordenar#Devuelve ordenar
def main():#Defino funcion principal
 ingresar=input("Ingresar palabras:").lower()#Le pido al usuario que ingrese las palabras
 lista=ingresar.split()#Separa las palabras ingresadas por el usuario
 lista_ordenada = ordenar_lista(lista)#Guardo la funcion ordenar lista
 print(lista_ordenada)#Imprime la lista ordenada
 
main()#Convencion:Llamamos a la funcion principal