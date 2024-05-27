#Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
#intercambie los valores de esas dos claves en el diccionario.
diccionario={"A":"1","B":"2"}#Creo el diccionario con sus dos valores
def cambiar_valores(diccionario):#Defino la funcion cambiar valores con el argumento diccionario
    clave1="A"#Creo una variable donde guarde la clave del primer valor
    clave2="B"#Creo una variable donde guarde la clave del segundo valor
    diccionario[clave1]="2"#Clave1 va a ser igual al valor de la segunda clave
    diccionario[clave2]="1"#Clave2 va a ser igual al valor de la primera  clave
    return diccionario#Devuelve el diccionario con los cambios de valor
print(diccionario)#Imprime el diccionario con la clave y valor sin cambiar
cambio=cambiar_valores(diccionario)#Guardo la funcion con su argumento
print(cambio)#Imprime el valor cambiado de las dos claves  