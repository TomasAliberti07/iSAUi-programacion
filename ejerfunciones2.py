#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
#valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
#máximo y el mínimo, utilizando la función anterior.
def calcularMaxMin(lista):#Inciar una funcion con el argumento lista
    mayor = lista[0]#Creo la variable maximo con el valor de la lista
    menor = lista[0]#Creo la variable minimo con el valor de la lista
    for numero in lista:#Hago un for que recorra los numeros de la lista
        if numero > mayor:#Verifico que numero sea mayor
            mayor = numero
        elif numero < menor:#Verifico que numero sea el menor
            menor = numero
    return mayor, menor#Pido que me devuelva el mayor y menor
numeros = input("Ingresa una lista de números separados por comas: ")#Le pido al usuario que ingrese los numeros
lista= [float(num) for num in numeros.split(",")]#Creo una lista  con el tipo de dato float y inicio un for que recorra los numeros de esa lista y el .split los divides en subcadenas con el valor de ","
resultadomax,resultadomin=calcularMaxMin(lista)#Guardo la funcion calcularmaxmin
print(f"El mayor es:{resultadomax} y el menor es:{resultadomin}")#Imrpimo los resultados
