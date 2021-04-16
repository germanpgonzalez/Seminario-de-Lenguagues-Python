def estructura_general(nombres,notas1,notas2):
   """ Devuelve la estructura de los alumnos, las dos notas
   y la suma de ambas """

   # Creo la lista de los alumnos y sus dos notas sumadas
   total = []
   for estu1, estu2 in zip(notas1, notas2):
       total.append(sum([estu1, estu2]))
   # Creo la lista final del alumno sus dos notas y la suma total
   alumnos = list(zip(nombres,notas1,notas2,total))
   return alumnos

def calcular_promedio(alumnos):
    """ Función que devuelve el promedio de las notas finales """
    suma = 0
    total = 0
    for est in alumnos:
        suma += int(est[3])
    total = suma / len(alumnos)
    print(f"\nEl promedio de las notas es: {total:.2f} ")

def ordenar_por_nombre(alumnos):
    """ Ordena la lista de alumnos por nombre. """
    ord1 = sorted(alumnos , key = lambda alumno: alumno[0])
    print()
    print(ord1)

def ordenar_por_nota1(alumnos):
    """ Ordena la lista de alumnos por las notas de la primer evaluación. """
    ord2 = sorted(alumnos , key = lambda alumno: alumno[1])
    print()
    print(ord2)

def ordenar_por_nota2(alumnos):
    """ Ordena la lista de alumnos por las notas de la segunda evaluación. """
    ord3 = sorted(alumnos , key = lambda alumno: alumno[2])
    print()
    print(ord3)

def ordenar_suma_notas(alumnos):
    """ Ordena la lista de alumnos por la suma de las notas. """
    ord4 = sorted(alumnos , key = lambda alumno: alumno[3])
    print()
    print(ord4)


def reporte_nota1(alumnos):
    """ Función que devuelve el reporte sobre la nota 1 """
    valinicio = int(input("Ingrese el valor de inicio del rango: \n"))
    valfinal = int(input("Ingrese el valor final del rango: \n"))
    reporte1 = list(filter(lambda alumnos: int(alumnos[1]) >= valinicio and int(alumnos[1]) <= valfinal, alumnos))
    print()
    print(reporte1)

def reporte_nota2(alumnos):
    """ Función que devuelve el reporte sobre la nota 2 """
    valinicio = int(input("Ingrese el valor de inicio del rango: \n"))
    valfinal = int(input("Ingrese el valor final del rango: \n"))
    reporte2 = list(filter(lambda alumnos: int(alumnos[2]) >= valinicio and int(alumnos[2]) <= valfinal, alumnos))
    print()
    print(reporte2)
    

def reporte_suma(alumnos):
    """ Función que devuelve el reporte sobre la suma de ambas notas """
    valinicio = int(input("Ingrese el valor de inicio del rango: \n"))
    valfinal = int(input("Ingrese el valor final del rango: \n"))
    reporte3 = list(filter(lambda alumnos: int(alumnos[3]) >= valinicio and int(alumnos[3]) <= valfinal, alumnos))
    print()
    print(reporte3)
    

def decision_de_reportes(ele):
    """ Recibe los resultados de menú y decide si hacer el reporte
        por "notas 1", por "notas 2" o por la suma de ambas; llamando a sus respectivas funciones."""

    if (ele == '1'):
        reporte_nota1(alumnos)
    elif(ele == '2'):
        reporte_nota2(alumnos)
    else:
        reporte_suma(alumnos)

def decision_de_orden(eleccion, alumnos):
    """ Recibe los resultados de menú y decide si hacer el ordenamiento
        por nombre, por "notas 1", por "notas 2" o por la suma de ambas; llamando a sus respectivas funciones."""

    if(eleccion == '1'):
        ordenar_por_nombre(alumnos)
    elif(eleccion == '2'):
        ordenar_por_nota1(alumnos)
    elif(eleccion == '3'):
        ordenar_por_nota2(alumnos)
    else:
        ordenar_suma_notas(alumnos)

def menu_opciones(alumnos):
    """ Crea un menú y envía los resultados a otras funciones
        para tomar decisiones. """

    while True:    #Los "while True" e "if", acompañados por el break, sirven de una suerte de equivalencia al "repeat-until". Son utilizados por si el usuario ingresa un valor erróneo.
        print(f"""
        {'*' * 17} Menu {'*' * 17}
        1 - Calcular promedio de los estudiantes.
        2 - Reportes.
        3 - Ordenar datos.
        0 - Salir.
        {'*' * 40}
        """)
        eleccion = input()

        if(eleccion == '0'):
            break   #Si es '0' termino el programa.
        
        elif(eleccion == '1'):
            calcular_promedio(alumnos)
        
        elif(eleccion == '2'):
            while True:
                print(f"""
                {'-' *40}
                ¿Sobre qué datos se hará el reporte?
                {'-' *40}
                1 - Notas 1.
                2 - Notas 2.
                3 - Suma de ambas notas.
                {'-' *40}
                """)
                eleccion = input()
                if(eleccion == '1' or eleccion == '2' or eleccion == '3'):
                    decision_de_reportes(eleccion) #Llama a la función de toma de decisiones de reportes.
                    break   #Este break y el de la elección 3 no terminan el programa, sólo el "while" de su elección.
        
        elif(eleccion == '3'):
            while True:
                print(f"""
                {'-' *40}
                 ¿Por qué criterio se ordenará?
                {'-' *40}
                1 - Por nombre.
                2 - Por nota en "Notas 1".
                3 - Por nota en "Notas 2".
                4 - Suma de ambas notas.
                {'-' *40}
                """)
                eleccion = input()
                if(eleccion == '1' or eleccion == '2' or eleccion == '3' or eleccion == '4'):
                    decision_de_orden(eleccion, alumnos) #Llama a la función de toma de decisiones de orden.
                    break


nombres = """"Agustin",
    "Alan",
    "Andrés",
    "Ariadna",
    "Bautista",
    "CAROLINA",
    "CESAR",
    "David",
    "Diego",
    "Dolores",
    "DYLAN",
    "ELIANA",
    "Emanuel",
    "Fabián",
    "Facundo",
    "Facundo",
    "FEDERICO",
    "FEDERICO",
    "GONZALO",
    "Gregorio",
    "Ignacio",
    "Jonathan",
    "Jonathan",
    "Jorge",
    "JOSE",
    "JUAN",
    "Juan",
    "Juan",
    "Julian",
    "Julieta",
    "LAUTARO",
    "Leonel",
    "LUIS",
    "Luis",
    "Marcos",
    "María",
    "MATEO",
    "Matias",
    "Nicolás",
    "NICOLÁS",
    "Noelia",
    "Pablo",
    "Priscila",
    "TOMAS",
    "Tomás",
    "Ulises",
    "Yanina","""

notas1 = """81,
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
 74"""

notas2 = """30,
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
 10"""

# Creo la lista de nombres 
nombres = nombres.replace('\"', '').replace(',', '').split()
# Creo la lista notas1
notas1 = notas1.replace(',', '').split()
# Paso la lista notas1 de Strings a enteros
notas1 = list(map(int,notas1))
# Creo la lista notas2
notas2 = notas2.replace(',', '').split()
# Paso la lista notas2 de Strings a enteros
notas2 = list(map(int,notas2))

alumnos = estructura_general(nombres,notas1,notas2)
menu_opciones(alumnos)
