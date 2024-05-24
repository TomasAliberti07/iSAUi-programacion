#Crear una función recursiva que permita calcular el factorial de un número. Realiza un
#programa principal donde se lea un número validado como entero, el cual es ingresado por
#el usuario y se muestre el resultado del factorial.
def calculo_factorial(numero):#Creo la funcion calcular factorial
 inicio= 1#Creo la variable incio con el valor de 1
 for n in range(1, numero + 1):#El bucle for a iterar los n segun el rango que yo diga en este caso desde 1 hasta el numero que ponga el usuario
        inicio *=n#Hago el calculo factorial
 return inicio#Devuelve el calculo 
def main():#Creo la funcion princial
     numero=int(input("Ingrese numero que desea calcular:"))#Le pido al usuario que digite el numero tipo int
     resultado= calculo_factorial(numero)#Guardo la funcion en esta variable
     print(f"El factorial de {numero} es: {resultado}")#Imprime el numero ingresado y su resultado

main()#Convecion 
