#Contar letras: Crea una función que tome una cadena como entrada y devuelva un
#diccionario con el recuento de cada letra en la cadena.
cadena=input("Ingrese la cadena:")#Pido al usuario que ingrese la cadena
def contar_letras(cadena):#Defino la funcion contar letras con el argumento cadena
    letras={}#Creo diccionario vacio
    for i in cadena:#Va a iterar todas las letras de cadena
     if i != " ": #i va a ignorar los espacios en blanco
        if i in letras:#Condiciono que si i esta en letras
            letras[i]+=1#le incremente
        else:
            letras[i]=1#En caso que no queda como esta
    return letras#Devuelve letras
contador=contar_letras(cadena)#Guardo la funcion 
print(contador)#imprimo el diccionario

