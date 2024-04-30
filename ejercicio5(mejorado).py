print("¿Cual es la conversion que desea hacer?")
print("1.Pasar de Celcius a Fahrenheit \n2.Pasar de Fahrenheit a Celcius ")
opciones=int(input("Elegir entre 1 o 2 para realizar la operacio:"))
def fahrent(celcius):
    fahrent=(celcius*9/5)+32
    return fahrent
def celcius(fahrent):
    celcius=(fahrent-32)*5/9
    return celcius
if opciones==1:
    celcius=float(input("Ingrese los C:"))
    fahrent=fahrent
    print("Da como resultado:",fahrent)
elif opciones==2:
    fahrent=float(input("Ingrese los F:"))
    celcius=celcius
    print("Da como resultado:",celcius)
else:
    print("La opcion que a ingresado es incorrecta")
