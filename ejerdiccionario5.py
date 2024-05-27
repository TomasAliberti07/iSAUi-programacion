#Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
#diccionario con los números de 1 a n como claves y sus cuadrados como valores.
n=10#Creo la variable 10 que va tener de valor 10
def recibir_num(n):#Creo la funcion recibir numero
    diccionario={}#Creo un diccionario vacio
    for i in range(1,n+1):#Hago un for que arranque del 1  y vaya iterando hasta n y i va tomando cada valor de n
        cuadrados=i**2#Hago el calculo matematico 
        diccionario[i]=cuadrados#Digo que valores que toma i esten en diccionario y sea igual a cuadrados osea que haga su potencia

    return diccionario #Devuelve el diccionario
resultado= recibir_num(n)#Guardo la funcion en la variable resultado
print(resultado)#Imprimo resultado

    