#Escribir un progama en Python que calcule el indice de masa corporal(IMC) de una persona.
peso=float(input("Ingrese su peso:"))#Le pido al usuario que ingrese su peso
altura=float(input("Ingrese su altura:"))#Le pido al usuario que ingrese su altura
calculo=peso/(altura**2)#Hago el calculo necesario
print("El IMC es de:", calculo)#Imrpimo el calculo