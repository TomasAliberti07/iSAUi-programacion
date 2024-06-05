#Contar palabras en frases: Escribe una función que reciba una lista de frases y
#devuelva un diccionario donde las claves son las palabras y los valores son las
#frecuencias de esas palabras en todas las frases.
def convertir_dic(diccionario):#Defino la funcion convertir dic
    for palabra in palabras:#Itera sobre cada palabra que ingrese el usuario
        diccionario[palabra]=palabras.count(palabra)#El diccionario va a tener como clave la palabra y el valor la cantidad de veces que aparezca con la funcion count
    return diccionario #Devuelve el diccionario

frase=input("Ingrese las palabras o frase : ").lower()#Le pido al usuario que ingrese la palabra o frase
palabras=frase.split(" ")#Por cada palabra que ingrese tiene que haber un espacio
diccionario={}#Creo diccionario vacio
conversor=convertir_dic(diccionario)#Guardo la funcion
print(conversor)#Imprimo el diccionario

