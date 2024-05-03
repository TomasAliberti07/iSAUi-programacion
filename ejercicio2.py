#Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros. 
#El programa debe solicitar al usuario que ingrese la cantidad en dólares
#y luego mostrar la cantidad equivalente en euros, utilizando un tipo de cambio fijo.
dolar=float(input("Ingrese cantidad de dolares:"))
tipo_cambio=0.93
euro= dolar*tipo_cambio
print(f"Equivale a {euro} euro ")