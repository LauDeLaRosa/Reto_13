def imprimir_valores_ascendente(diccionario):  #Se define la funcion
    valores = sorted(diccionario.values()) #Se usa para ordenar los valores de forma ascendente
    for valor in valores: #Se itera sobre la lista de valores
        print(valor) #Se imprime cada valor

# Ejemplo 
mi_diccionario = {
    'a': 5,
    'b': 2,
    'c': 8,
    'd': 1
}

imprimir_valores_ascendente(mi_diccionario)
