import random
numeroaleatorio=random.randint(1,100)
intento=0
print("....Bienvenido al juego numeros magicos....\n #La consigna del juego es acertar al numero del 1 al 100 a traves de pistas")
print("....¿Estas listo?....")
empezar=input("Responde Si o No:").lower()
if empezar=="si":
    print("Bien comencemos")
elif empezar=="no":
    print("Hasta la proxima:)")
else: 
    print("Respuesta no valida")
