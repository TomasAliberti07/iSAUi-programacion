#Escribir un progama en Python que calcule el indice de masa corporal(IMC) de una persona.
peso=float(input("Ingrese su peso:"))
altura=float(input("Ingrese su altura:"))
calculo=peso/(altura**2)
print("El IMC es de:", calculo)