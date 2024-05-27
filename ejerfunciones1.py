#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , tú “. 
#Crea un programa principal donde se use dicha función luego del ingreso del usuario.

def Converti_Espacio(texto):#Defino la funcion Converti_Espacio con el argumento texto
    espacio = "-"#Defino una variable que se llame espacio y guarde un guion
    lista = []  # Crear una lista vacía para almacenar las letras espaciadas
    for letra in texto:#Incio un for que recorrar las letras del texto
        lista.append(letra + espacio)  # Agregar cada letra seguida de un guión
    return "".join(lista)  # Unir todas las letras espaciadas en un solo texto

def principal():#Definos la funcion principal
    texto = input("Ingrese el texto que desea espaciar: ")#Le pedimos al usuario que ingrese la palabra o texto que desea espaciar
    conversor = Converti_Espacio(texto)#Guardamos la funcion Converti_Espacio
    print(f"{conversor}")#Imprimo la palabra espaciada

principal()
