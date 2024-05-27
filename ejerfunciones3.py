#Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
#función en un programa principal que lea el radio de una circunferencia y muestre su área y
#perímetro.
import math#Importo la libreria math para poder hacer el calculo del area y el perimetro
radio=float(input("Ingrese el radio de la circunferencia:"))#Le digo al usuario que ingrese el valor del radio
def calculo_area_perimetro(radio):#Defino la funcion que va a calcular el area y perimetro
       perimetro=2* math.pi* radio#Ingreso la variable perimetro y que haga la cuenta con el import math
       area= math.pi * radio **2#Ingreso la varibale area y que haga la cuenta con el import math
       return perimetro, area#Devuelve el resultado del perimetro y area
r_perimetro,r_area=calculo_area_perimetro(radio)#Guardo la funcion 
print(f"El perimetro de la circunferencia es:{r_perimetro} y el area de la circunferencia es:{r_area}")#Imprimo el resultado
