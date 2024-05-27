import random
numero_aleatorio=random.randint(1,100)
intentos=0
print("....Bienvenido al juego numeros magicos....\n #La consigna del juego es acertar al numero del 1 al 100 ")
print("....¿Estas listo?....")
empezar=input("Responde Si o No:").lower()
if empezar=="si":
    print("Bien comencemos")
elif empezar=="no":
    print("Hasta la proxima:)")
else: 
    print("Respuesta no valida")
    volver=input("Por favor responda si o no:").lower()
while True:
     intento= int(input("Ingrese un numero: "))
     intentos= intentos + 1
     if intento < numero_aleatorio:
          print("EL numero es demasiado bajo")
     elif intento > numero_aleatorio:
          print("El numero es muy alto") 
     else:
          print("Felicidades adivinaste el numero hasta luego:)")
          break