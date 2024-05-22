#Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
#nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
#diccionario).
diccionario1={"a":"1","b":"2","c":"3"}#Creo el primer diccionario con su clave valor
diccionario2={"d":"4","e":"5","f":"6"}#Creo el segundo diccionario con su clave valor
def combinar_diccionario(diccionario):#Defino la funcion combinar diccionario con el argumento diccionario
    diccionario3={}#Creo el tercer diccionario vacio que es donde se combinaran ambos diccionarios
    diccionario3.update(diccionario1)#Agrego la clave y el valor del primer diccionario(con la funcion upddate)
    diccionario3.update(diccionario2)#Agrego la clave y el valor del segundo diccionario(con la funcion update)
    return diccionario3#Devuelve el tercer diccionario 
dic= combinar_diccionario("")#Guardo la funcion en la variable dic
print(dic)#Imprime el resultado