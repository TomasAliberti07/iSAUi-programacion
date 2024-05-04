print("Bienvenido al conversor de temperatura")
temperatura=float(input("Ingrese la temperatura:"))
escala=input("Elija la escala en que desee convertilo Fahrenheit(F) o Celcius(C):").upper()
if escala=="F":
    celcius=(temperatura * 5/9) + 32
    print(celcius)
elif escala=="C":
    fahrenheit= (temperatura - 32)*5/9
    print(fahrenheit)
else: 
    print("No es correcta la conversion que desea realizar intentelo de nuevo...")

