#Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
#valor máximo y el mínimo de la lista.
def Calculomaxmin(lista):#Defino la funcion Calculomaxmin con el argumento lista
    mayor=max(lista)#defino la variable mayor con la funcion max
    menor=min(lista)#defino la variable menor con la funcion min
    return mayor, menor #Devuelve el mayor y menor
numeros=(input("Ingrese los numeros con coma de la lista:" ))#Le digo al usuario que digite los numeros con coma
numeros=[float(num) for num in numeros.split(",")]#Creo la lista y el for recorre cada uno de los numeros de la lista 
rmayor,rmenor= Calculomaxmin(numeros)#Guardo la funcion Calculomaxmin dentro de estas variables
print(f"El mayor es:{rmayor}y el menor es:{rmenor}")#Imrpimo los resultados
    