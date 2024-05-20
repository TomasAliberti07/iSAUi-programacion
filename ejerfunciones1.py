#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , tú “. 
#Crea un programa principal donde se use dicha función luego del ingreso del usuario.

def Converti_Espacio(texto):
    espacio = "-"
    lista = []  # Crear una lista vacía para almacenar las letras espaciadas
    for letra in texto:
        lista.append(letra + espacio)  # Agregar cada letra seguida de un guión
    return "".join(lista)  # Unir todas las letras espaciadas en un solo texto

def principal():
    texto = input("Ingrese el texto que desea espaciar: ")
    conversor = Converti_Espacio(texto)
    print(f"{conversor}")

principal()