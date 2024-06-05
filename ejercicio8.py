<<<<<<< HEAD
import random
import string
def contraseña(longitud=12):
    caracter= string.ascii_letters + string.digits + string.punctuation
    contraseña="".join(random.choice(caracter) for i  in range (longitud))
    return contraseña

longitudmin=12        
crea_contraseña= contraseña(longitudmin)
print("Su contraseña es:", crea_contraseña)
=======
import random
import string
def contraseña(longitud=12):
    caracter= string.ascii_letters + string.digits + string.punctuation
    contraseña="".join(random.choice(caracter) for i  in range (longitud))
    return contraseña

longitudmin=12        
crea_contraseña= contraseña(longitudmin)
print("Su contraseña es:", crea_contraseña)
>>>>>>> 46ab3dd27299fd70e777ef512e65a271ce61e649
 