#Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
#valores únicos en el diccionario.
diccionario={"blue":"azul","red":"rojo","green":"verde"}#Creo el diccionario
def valor_unico(diccionario):#Defino la funcion valor unico
   cambio=list(diccionario.values())#Los valores del diccionario se guardan en una lista de valor unico
   return cambio#Devuelve el cambio
unico_valor=valor_unico(diccionario)#Guardo la funcion
print(unico_valor)#Imprime  cambio