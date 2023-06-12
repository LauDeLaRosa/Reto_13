def mezclar_diccionarios(dic1, dic2): #Se define la funcion
    dic_mezclado = dict(dic2)  # Crear una copia del segundo diccionario

    for clave, valor in dic1.items(): #iteramos sobre las claves y valores del primer diccionario
        if clave not in dic_mezclado: 
            dic_mezclado[clave] = valor

    return dic_mezclado

# Ejemplo 
diccionario1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

diccionario2 = {
    'b': 20,
    'd': 40,
    'e': 50
}

diccionario_mezclado = mezclar_diccionarios(diccionario1, diccionario2)
print(diccionario_mezclado)
