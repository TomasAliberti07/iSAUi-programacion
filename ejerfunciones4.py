#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
#devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
#hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
#3 oportunidades.
def Login(usuario, contraseña,intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        intentos += 1
        print(f"Usuario o contraseña incorrecta. Intentos restantes: {3 - intentos}")
        return False

def Validar_Intentos(intentos):
    if intentos >= 3:
        print("Ha superado la cantidad de intentos.")
        return False
    return True

intentos = 0
while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if Login(usuario, contraseña,intentos):
        print("Bienvenido usuario1")
        break
    else:
        if not Validar_Intentos(intentos):
            break