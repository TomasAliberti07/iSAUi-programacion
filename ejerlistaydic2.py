#Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
#un diccionario donde las claves son las longitudes de las palabras y los valores son
#listas de palabras con esa longitud.
palabra = input("Ingrese una palabra o varias: ")#Le pido al usuario que ingrese las palabras
palabras = palabra.split(" ")#Cada palabra que ingrese el usuario va separada por espacio
def longitud_pala(palabras):#Defino la funcion 
    diccionario = {}#Creo diccionario vacio
    for palabra in palabras:#Itera sobre cada palabra 
        longitud = len(palabra)#Longitud de cada palabra
        if longitud in diccionario:#Si la longitud esta en la palabra 
            diccionario[longitud].append(palabra)#Agrega la palabra con esa longitud a una lista
        else:
            diccionario[longitud] = [palabra]#Si no crea otra lista con esa longitud
    return diccionario#Devuelve diccionario
agrupacion = longitud_pala(palabras)#Guardo la funcion
for longitud, lista_palabras in agrupacion.items():#Itera sobre longitud y lista de palabras 
    print(f"Longitud {longitud}: {lista_palabras}")#Imprime la longitud y la lista de palabras