#Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
#tuplas (clave, valor) y actualice el diccionario con esas tuplas.
diccionario={"A":1,"B":2, "C":3}#Creo el diccionario
tuplas=("D",4,"E",5,"F",6)#Creo la tupla
def actualizar_dic(tuplas):#Defino la funcion actualizar dic
    ndiccionario=dict(diccionario)#Creo una copia del diccionario original y la guardo en uno nuevo, dict es una clase que permite la copia del diccionario
    for i in range(0,len(tuplas),2):#Crea un rango de numeros desde 0 hasta la longitud de la tupla avanzando 2 en 2
        ndiccionario[tuplas[i]]=tuplas[i+1]#Cada vezñ que itere la posion de la tupla le va a asociar el valor que esta por delante
    return ndiccionario#Devuelve el ndiccionario
nuevo_dic=actualizar_dic(tuplas)#Guardo la funcion 
print(nuevo_dic)#Imprimo el nuevo diccionario
