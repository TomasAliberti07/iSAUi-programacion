<<<<<<< HEAD
#Crea un juego que le pida al usuario que piense un número entre 1 y 100. Luego, 
#el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
#En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual 
#al número propuesto por el programa. El juego debe terminar cuando el programa adivine el número correcto.
print("¡Piensa un numero del 1 al 100 tratare de adivinar!")
numero=input("Preciona enter para comenzar :)")

comienzo=1
final=100

while True:
    numero_adivinar= (comienzo + final)//2
    respuesta=input(f"El numero es {numero_adivinar} cierto? (mayor/menor/igual):").lower()
    if respuesta=="igual":
        print("Lo sabía :) tu numero es:", numero_adivinar)
        break
    elif respuesta=="mayor":
        comienzo= numero_adivinar+1
    elif respuesta=="menor":
         final= numero_adivinar-1
#Crea un juego que le pida al usuario que piense un número entre 1 y 100. Luego, 
#el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
#En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual 
#al número propuesto por el programa. El juego debe terminar cuando el programa adivine el número correcto.
print("¡Piensa un numero del 1 al 100 tratare de adivinar!")
numero=input("Preciona enter para comenzar :)")

comienzo=1
final=100

while True:
    numero_adivinar= (comienzo + final)//2
    respuesta=input(f"El numero es {numero_adivinar} cierto? (mayor/menor/igual):").lower()
    if respuesta=="igual":
        print("Lo sabía :) tu numero es:", numero_adivinar)
        break
    elif respuesta=="mayor":
        comienzo= numero_adivinar+1
    elif respuesta=="menor":
         final= numero_adivinar-1
    else:
        print("Respuesta no valida")