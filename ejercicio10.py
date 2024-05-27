import random#Importo random

def selec_palabra():#Defino la funcion 
    palabras = ("computadora", "ram", "software", "carpeta", "guardar", "caracter")#Creo una tupla con las palabras a adivinar
    adiv_palabra = random.choice(palabras)#Elije una palabra al azar de la tupla
    return adiv_palabra#Devuelve la palabra para adivinar

def tablero(palabra, letra_adivinada):#Defino la funcion tablero
    mostrar_palabra = ""
    for letra in palabra:#Va a iterar por cada letra de la palabra
        if letra in letra_adivinada:#Si la letra se encuentra en las letras de la palabra
            mostrar_palabra += letra #Muestra la letra en el tablero
        else:
            mostrar_palabra += "_"#Si no esta queda el espacio vacio
    return mostrar_palabra#Devuelve en el caso de if o else

intentos = 6#Creo la variable intentos con el valor de 6
letracorrecta = []
palabra_oculta = selec_palabra()

while intentos > 0:#Creo un bucle while
    letra_usuario = input("Ingresa una letra: ").lower()  # Solicita al usuario que ingrese una letra
    if letra_usuario.isalpha() and len(letra_usuario) == 1:  # Verifica que la entrada sea una sola letra
        if letra_usuario in letracorrecta:#Verifica que la letra que ingreso el usuario sea correcta
            print(f"Ya adivinaste la letra '{letra_usuario}'.")#Imprime mensaje
        elif letra_usuario in palabra_oculta:#Verifica que la letra del usuario este en palabra oculta
            letracorrecta.append(letra_usuario)#Agrega la letra 
            print(f"¡Correcto! La letra '{letra_usuario}' está en la palabra.")#Imprime mensaje
        else:#Si la letra no esta
            intentos -= 1#Resta un intento de los 6
            print(f"La letra '{letra_usuario}' no está en la palabra. Te quedan {intentos} intentos.")#Imprime el mensaje
    else:#En el caso que no ingrese una letra o mas de una
        print("Ingresa una sola letra válida.")#Imprime mensaje

    palabra_mostrada = tablero(palabra_oculta, letracorrecta)#Guardo la funcion tablero 
    print(f"Palabra actual: {palabra_mostrada}")#Imprime la palabra

    if palabra_mostrada == palabra_oculta:#Verifica si la palabra es palabra oculta
        print("¡Felicidades! Has adivinado la palabra.")#Imprime mensaje
        break#Termina el ciclo while

if intentos == 0:#Verifica si el contandor de intentos llego a cero
    print(f"¡Perdiste! La palabra era '{palabra_oculta}'.")#Imprime la palabra oculta