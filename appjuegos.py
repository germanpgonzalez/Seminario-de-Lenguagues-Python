import csv

# Abro el archivo CVS


archivo = open("appstore_games.csv", "r", encoding='utf-8')

csvreader = csv.reader(archivo, delimiter=',')

# Imprimo el encabezado del archivo CSV

encabezado = next(csvreader)
print()
print(encabezado)
print()
print()
# Imprimo los juegos gratuitos en idioma español
print("Juegos gratuitos en español: ")
print()
for linea in csvreader:
    if linea[12] == "ES" and linea[7] == '0':
        print(linea[2])

print()



archivo.close()