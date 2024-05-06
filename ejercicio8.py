import random
import string
def contraseña(longitud=12):
    caracter= string.ascii_letters + string.digits + string.punctuation
    contraseña="".join(random.choice(caracter) for i  in range (longitud))
    return contraseña

longitudmin=12        
crea_contraseña= contraseña(longitudmin)
print("Su contraseña es:", crea_contraseña)
 