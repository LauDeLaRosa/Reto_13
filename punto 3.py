import json

# Función para leer el archivo JSON
def leer_json(archivo):
    with open(archivo, 'r') as file:
        data = json.load(file)
    return data

# Función para imprimir los nombres completos de personas que practican un deporte específico
def imprimir_nombres_deporte(data, deporte):
    for usuario, info in data.items():
        if deporte in info['deportes']:
            nombres = info['nombres']
            apellidos = info['apellidos']
            nombre_completo = f"{nombres} {apellidos}"
            print(nombre_completo)

# Función para imprimir los nombres completos de personas en un rango de edades
def imprimir_nombres_rango_edades(data, edad_min, edad_max):
    for usuario, info in data.items():
        edad = info['edad']
        if edad_min <= edad <= edad_max:
            nombres = info['nombres']
            apellidos = info['apellidos']
            nombre_completo = f"{nombres} {apellidos}"
            print(nombre_completo)

# Programa principal
archivo_json = 'datos.json'
data = leer_json(archivo_json)

# Solicitar al usuario el deporte y mostrar los nombres de personas que lo practican
deporte_ingresado = input("Ingrese el deporte: ")
print("Nombres de personas que practican", deporte_ingresado)
imprimir_nombres_deporte(data, deporte_ingresado)

# Solicitar al usuario el rango de edades y mostrar los nombres de personas dentro de ese rango
edad_minima = int(input("Ingrese la edad mínima: "))
edad_maxima = int(input("Ingrese la edad máxima: "))
print("Nombres de personas en el rango de edades", edad_minima, "-", edad_maxima)
imprimir_nombres_rango_edades(data, edad_minima, edad_maxima)
