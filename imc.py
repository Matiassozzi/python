#script IMC en base a datos proporcionados por user

import math
from tabulate import tabulate


peso = float(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ingrese su estatura en metros: "))

IMC = round(peso/math.pow(altura,2),1) #calculo de imc es altura en cm al cuadrado / peso#


lista = [["Resultado","Indice de masa corporal"],["Peso mas bajo al normal","Menos de 18.5"],["Normal","18.5 – 24.9"],["Peso mas alto al normal","25.0 – 29.9"],["Obesidad","Más de 30.0"]]

print(tabulate(lista))

print("Resultado")
print("Su indice de masa corporal es de "+str(IMC))