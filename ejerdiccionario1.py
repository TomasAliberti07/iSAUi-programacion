#Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
#con la frecuencia de cada letra en la cadena.
def contar_letras(cadena):#Definimos la funcion contar letras con el argumento cadena
    diccionario={}#Creamos un diccionario vacio para las frecuencias
    for letra in cadena:#Un for que recorra las letras de la cadena
     if letra!=" ": #En el caso que haya un espacio hago que lo ignore
      letra=letra.lower()#Convertimos la letra en minuscula para que no haya diferencia entre mayuscula y minuscula
     if letra in diccionario:#Verifico que la letra se encuentre en el diccionario
         diccionario[letra] +=1#En el caso que se repita la letra  se incrementa
     else:
        diccionario[letra]= 1#En el caso que se encuentre una vez se queda con el valor de 1
    return diccionario
palabra=input("Ingrese la palabra:")
cadenas=contar_letras(palabra)
print(cadenas)