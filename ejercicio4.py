#Ejercicio 4: Contador de Palabras
#Desarrolla un programa en Python que solicite al usuario que ingrese una frase y 
#luego cuente y muestre el número de palabras en esa frase.

frase=input("Ingrese alguna frase:")
palabras=frase.split()
contpalabras=len(palabras)
print("La cantidad de palabras son:",contpalabras)