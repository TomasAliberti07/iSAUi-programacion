#Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
#y devuelva un nuevo diccionario solo con las claves especificadas.
diccionario={"Nombre":"Carlos","Apellido":"Gustos","Edad":"34"}#Creo el diccionario 
def filtrar_diccionario(diccionario,claves):#Creo la funcion con los argumentos diccionario y claves
    n_diccionario={}#Creo un nuevo diccionario
    for clave in claves:#Un for que reccorre las claves del diccionario
      if clave in diccionario:#Condiciono que si la clave esta en el diccionario  
         n_diccionario[clave]=diccionario[clave]#Va agregar la clave al nuevo diccionario con el valor que tiene cada una
    return n_diccionario# Me va a devolver el nuevo diccionario
         
claves=["Nombre", "Apellido","Gustos","Edad"] #Creo una lista con las claves
las_claves=filtrar_diccionario(diccionario,claves)#Guardo la funcion en la variable 
print(las_claves)#Imprime las claves con su valor
