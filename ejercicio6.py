#Escribe un programa en Python que valide una contraseña ingresada por el usuario. 
#La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y 
#un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no
print("Escriba una contraseña que contenga al menos 8 caracteres,una mayuscula,un numero y un caracter especial(#$%&/()=?¡¿):")
contraseña=input("")
while True:
 if  len(contraseña)>=8 :
    if any(c.isupper() for c in contraseña):#if any verifica si la contraseña contiene al menos una mayuscula y for que recorra cada palabra o digito de la contraseña
        if any(c.islower() for c in contraseña):#Verifica si tiene minuscula con la funcion islower y lo recorre por un for 
            if any(c in ".:;,!#$%&/()=?¡¿" for c in contraseña):#Verifica si contiene uno de los caracteres especiales
            
                if any(c.isdigit() for c in contraseña):#Verifica si contiene al menos un numero
                     print("La contraseña fue creada correctamente :)")
                     break
 else:
    print("Hubo un error por favor vuelva a intentarlo...")
    input("")
