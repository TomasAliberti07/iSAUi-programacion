#Promedio de una lista: Crea una función que calcule el promedio de los números en
#una lista dada.
def sacar_prom(lista):#Definimos la funcion sacar promedio
    suma = 0#Defino la variable suma
    for num in lista:#Un for que recorre los numeros de la lista
        suma += num#Sumo todos los numeros de la lista
    promedio = suma / len(lista)#Saco el promedio con la suma y la longitud de la lista
    return promedio#Devuelve el promedio
numeros = input("Ingrese los números de la lista separados por comas: ")#El usuario ingresa los datos numericos
lista_numeros = [float(nume) for nume in numeros.split(",")]#Creo la lista vacia con valores float y que un for recorra la lista y por cada numero ponga una coma
promedio = sacar_prom(lista_numeros)#Guardo la funcion en promedio
print(f"El promedio es:{promedio}")#Imrpimo el resultado