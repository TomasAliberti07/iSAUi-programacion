#Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
#nuevo que invierta las claves y los valores.
diccionario1={"rojo":"red", "verde":"green", "azul": "blue", "negro": "black"}#Creo el diccionario con su clave valor
def invertir_dic(diccionario):#Defino la funcion invertir diccionario con el argumento diccionario
    diccionario_inver={}#Creo un diccionario vacio
    for clave, valor in diccionario1.items():#Recorre el primer diccionario y itera la clave y el valor de cada uno
        diccionario_inver[valor]=clave#Cambio la clave por el valor y viseversa
    return diccionario_inver#Devuelve el diccionario invertido
resultado= invertir_dic(diccionario1)#Guardo la funcion de invertir diccionario
print(resultado)#Imprime el diccionario invertido
