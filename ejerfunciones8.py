#Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
#lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
#de puntuación.
def palindromo(texto):#Defino la funcion palindromo con el argumento texto
    texlimpio = "".join(c.lower() for c in texto if c.isalnum())#Unimos en una cadena el texto y que tenga todo en minuscula y verifique que sean alfanumericos
    return texlimpio == texlimpio[::-1]#Va a devolver solamente si es un palindromo
def main():#Definimos funcion principal
  frase = input("Ingrese una frase,palabra o numero para saber si es un palindromo o no: ")#Le pido al usuario que ingrese los datos
  if palindromo(frase):#Verifica que sea un palindromo
    print(f"'{frase}' es un palíndromo.")#Imprime mensaje que si es
  else:#En el caso que no
    print(f"'{frase}' no es un palíndromo.")#Imprime mensaje que no es
main()#Convencion:Llamamos a la funcion principal