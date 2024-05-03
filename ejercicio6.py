#Escribe un programa en Python que valide una contraseña ingresada por el usuario. 
#La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y 
#un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no
print("Escriba una contraseña que contenga al menos 8 caracteres,una mayuscula,un numero y un caracter especial(#$%&/()=?¡¿):")
contraseña=input("")
if  len(contraseña)>=8 :
    contraseñam=["A-Z"]
    contraseñamin=["a-z"]
    contraseñasim=["!#$%&/()=?¡¿"]
    contraseñanum=[1234567890]
    print("La contraseña fue creada correctamente :)")
else:
    print("Hubo un error por favor vuelva a intentarlo...")