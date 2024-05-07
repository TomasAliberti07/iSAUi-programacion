#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. 
#El factorial de un número entero positivo n se define como el producto de todos los enteros positivos 
#menores o iguales a n. El programa debe manejar números enteros grandes y mostrar el resultado.

def calculo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero=int (input("Ingrese el numero que desea calcular:"))
print(f"El factorial de {numero} es: {calculo(numero)}")