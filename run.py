# Ingresas un numero natural y te devuelve si es multiplo de 2, de 3 o 5

numero = int(input("Ingrese un numero natural: \n"))
if numero %2 == 0:
 print(f"{numero} es multiplo de 2")
elif numero %3 == 0:
 print(f"{numero} es multiplo de 3")
else:
 print(f"{numero} es multiplo de 5") 