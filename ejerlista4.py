#Elementos mayores que un valor: Escribe una función que tome una lista de números
#y un valor n, y devuelva una nueva lista con los elementos mayores que n.
lista=[1,2,3,4,5,6,7,8,9,10]#Creo la lista con sus elementos
n=5#Creo la variable "n" que tiene un valor int que es "5"
def mayores_que_n(lista, n):#Creo la funcion de mayores_que_n con los argumentos lista, n
    listan=[]#Creo una nueva lista vacia
    for n in lista:#Hago un for que recorra los numeros de la lista
        if n > 5:#Condiciono que si n es mayor a 5 
         listan.append(n)#Va a Agregar a la nueva lista los numeros mayores a 5
    return listan#Le pido que me devuelva la lista nueva
resultado=mayores_que_n(lista,n)#Guardo la funcion 
print(resultado)#Imprimo la nueva lista con los valores mayor a 5