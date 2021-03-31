nombres = ''' 'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina' '''.replace(',', '').replace(" \' " , '')

notas1 = '''81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74'''.replace(',', '').replace('\'', '')

notas2 = '''30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10'''.replace(',', '')


# Creo la lista de nombres 
nombres = nombres.split()
# Creo la lista notas1
notas1 = notas1.split()
# Creo la lista notas2
notas2 = notas2.split()


# Creo la lista de los alumnos y sus dos notas
nombres_notas = list(zip(nombres,notas1,notas2))


# Creo una lista con las dos notas sumadas
# Calculo la suma total de las notas y la cantidad de notas en total
total = []
suma = 0
prom = 0
cant = 0
for est in nombres_notas:
    total.append(int(est[1])+ int(est[2]))
    suma += int(est[1]) + int(est[2])
    cant += 1

# Calculo el promedio de las notas
prom = suma / cant

# Creo la lista final del alumno y su nota final
lista_final = list(zip(nombres,total))


# Verifico que alumno obtuvo menos del promedio
for est in lista_final:
    if int(est[1]) < prom:
     print(f"\nEl alumno {est[0]} tiene nota {est[1]} y esta debajo del promedio")

print()
