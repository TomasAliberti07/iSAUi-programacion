#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.
palabras=input("Ingrese las palabras separadas por coma:")#Ingresar las palabras
palabras=palabras.split(",")#Separar por coma cada palabra
lista=palabras#Las palabras se guardan en una lista
def frecuencias(lista):#Defino la funcion frecuencias con el argumento lista
    diccionario={}#Creo un diccionario vacio
    for palabra in lista:#Va a iterar sobre cada palabra de la lista
        if palabra in diccionario:#Si la palabra esta en el diccionario 
            diccionario[palabra]+=1#Aumenta la frecuencia en 1
        else:
            diccionario[palabra]=1#Si la palabra no esta en el diccionario la agrega con una frecuencia de 1
    return diccionario#Devuelve diccionario
las_frecuencias=frecuencias(palabras)#Guardo la funcion 
print(las_frecuencias)#Imprimo el diccionario con las frecuencias

