import PySimpleGUI as sg
import csv,json

def opcion1():
 """ Función que devuelve 10 series o peliculas con más de 7 puntos de imdb raiting """

 try:
     archivo_disney = open("disney_plus_shows.csv", "r")
 except FileNotFoundError:
     sg.popup_error("El archivo CSV no fue encontrado")
 else:
     csvreader = csv.reader(archivo_disney, delimiter = ',')
     encabezado = next(csvreader)
     print()
     print(encabezado)

     # Analisis del archivo CSV
     data = []
     bandera = True
     cant = 0
     maximo = 10
     imdb_raiting = '7.0'
     while bandera:
         for linea in csvreader:
             if linea[17] > imdb_raiting:
                 data.append({"Title: ": linea[1], "Year: ": linea[5], "Genere: ":linea[9], "Imdb Raiting: ":linea[17]})
                 archivo_json = open("disney.json","w")
                 json.dump(data,archivo_json, indent = 4)
                 archivo_json.close()
                 cant += 1
                 if cant == maximo:
                     bandera = False
                     break
     archivo_disney.close()
   

def opcion2():
 """ Función que devuelve 10 países con más de 2.000.000 casos de covid confirmados"""

 try:
     archivo_covid = open("worldometer_coronavirus_summary_data.csv", "r")
 except FileNotFoundError:
     sg.popup_error("El archivo CSV no fue encontrado")
 else:
     csvreader = csv.reader(archivo_covid,delimiter = ',')
     encabezado = next(csvreader)
     print()
     print(encabezado)

     # Análisis del archivo CSV
     data = []
     bandera = True
     cant = 0
     maximo = 10
     casos_confirmados = 2000000
     while bandera:
         for linea in csvreader:
             if int(linea[2]) > casos_confirmados:
                 data.append({"Pais: ":linea[0], "Continente: ":linea[1], "Casos confirmados: ":linea[2]})
                 archivo_json = open("covid19.json","w")
                 json.dump(data,archivo_json, indent = 4 )
                 archivo_json.close()
                 cant += 1
                 if cant == maximo:
                     bandera = False
                     break
     archivo_covid.close()

# Tamaño de los botones y pad

tam_button = (800,3)
pad_button = (100,8)

# Defino los elementos gráficos: Textos, input, botones.

layout = [
    [sg.Text("¿Qué datos analizamos?",size=(38, 1), text_color = 'purple', justification='center', font=("Helvetica", 15))],
    [sg.Button('Disney Plus', pad = pad_button, size = tam_button, key = '-OPTION1-')],
    [sg.Button('Casos Covid-19', pad= pad_button, size = tam_button, key = '-OPTION2-')],
    [sg.Button('Salir', pad = pad_button, size = tam_button, key = '-EXIT-')]]

# Creo la ventana con el layout definido
windows = sg.Window('Actividad 1 x Python Plus - TEORÍA -', layout, size= (380,280), resizable= False, disable_close= True)

while True:
 event,values = windows.read()
 print(f"EVENTO: {event}")
 print(f"VALORES: {values}")

 # El evento por defecto para cerrar la ventana es Salir.
 if event == sg.WINDOW_CLOSED or event == '-EXIT-':
     break

 # El evento de la opción 1:
 if event == '-OPTION1-':
     opcion1()

 # El evento de la opción 2:
 if event == '-OPTION2-':
     opcion2()

# Cierre de la ventana
windows.close()