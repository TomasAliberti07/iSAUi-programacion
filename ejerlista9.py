#Producto de elementos: Escribe una función que tome una lista de números y
#devuelva el producto de todos los elementos.
numeros=(input("Ingrese los numeros de la lista con coma uno despues del otro:"))#Le pido al usuario que ingrese los datos
lista=[int(num)for num in numeros.split(",")]#Creo la lista 
def producto_numeros(lista):#Defino la funcion de  producto
    producto=1#Creo la variable numero que va a guardar el valor de uno
    for i in lista:# Va a iterar cada numero de la lista
        producto *= i#Cada numero que tome i lo va a multiplicar por 1 y lo va guardando sucesivamente
    return producto#Devuelve el producto
resultado=producto_numeros(lista)#Guardo la funcion
print(f"El producto de todos los elementos de la lista es: {resultado}")#Imprimo el producto de todos los elementos
