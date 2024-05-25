#Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
#devuelva la suma de todos los valores.
diccionario={"a":1,"b":2,"c":3,"d":4,"e":5}#Crea un diccionario con su clave valor
def sumar_valores(diccionario):#Defino la funcion  suma de valores con el argumento diccionario
    suma=0#Creo la variable suma con el valor de 0
    for valor in diccionario.values():#El valor va a tomar cada valor de el diccionario
        suma+=valor#Suma de los valores
    return suma#Pido que me devuelva la suma
resultado=sumar_valores(diccionario)#Guardo la funcion 
print(f"La suma de las valores es:{resultado}")#Imprimo el resultado
