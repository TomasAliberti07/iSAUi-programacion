#Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.
numeros=input("Ingrese los numeros de la lista separados por coma:")#Le pido al usuario que ingrese los numeros
lista=[int(num)for num in numeros.split(",")]# Los numeros que ingresa el usuario se van a guardar en la lista solamente si escribe la coma despues de cada numero
def buscar_valor(lista):#Defino la funcion buscar valor
    for i in range(len(lista)):#Un for que itere el rango del indice de la lista
        if lista[i]==valor:#Condiciono que si el valor ingresado esta en el indice
         return i#Devuelva el indice del numero que se encuentra en la lista
    return -1#En caso que no este en la lista devuelve -1
valor=int(input("Ingrese un numero de la lista para buscar su indice:"))#Le pido al usuario que ingrese el indice que tiene el numero
resultado=buscar_valor(lista)#Guardo la funcion 
print(f"El indice es: {resultado}")# Imprime el resultado

