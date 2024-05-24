#Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
#los números pares en la lista.
lista=[1,2,3,4,5,6,7,8,9,10]#Creo una lista con sus elementos
def suma_pares(lista):#Hago una funcion de suma de pares con el argumento lista
    n=0#Creo la variable n con un valor de 0
    for i in lista:# i toma cada numero de la lista
        if i %2==0:# Condiciono que  si en calculo de i/2 es resto 0 el numero es par
            n=n+i#En el caso que se cumpla la condicion n va acumulando los valores i 
    return n #Devuelve n
def principal():#Creo la funcion principal
 resultado= suma_pares(lista)#Guardo la funcion de suma de pares
 print(f"la suma de los  de los pares de la lista {lista} es: {resultado}")#Imprimo la funcion 

principal()#Convencion 