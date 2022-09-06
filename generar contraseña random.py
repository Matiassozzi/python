from sre_constants import LITERAL_IGNORE
import string
import random


## caracteres para generar la contraseña
caracteres = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generar_contraseña():
	## largo de la contraseña
	largo = int(input("Ingresa el largo de la contraseña : "))

	## Mezclar caracteres
	random.shuffle(caracteres)
	
	## Elegir caracteres random de la lista
	contraseña = []
	for i in range(largo):
		contraseña.append(random.choice(caracteres))

	## Mezclar el resultado
	random.shuffle(contraseña)

	## convertir la lista a string
	## imprimir la lista
	print("".join(contraseña))



## invocar la funncion
generar_contraseña()