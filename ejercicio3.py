def number_spiral (fila, columna):
    #Verifica si la fila es mayor que la columna
    if fila > columna:
        #Verifica si la fila es par
        if fila % 2 == 0:
            #Verifica si la fila es par, calcula el resultado usando la formula
            resul_fila = (fila**2 - columna +1)
            return resul_fila 
        #Si la fila es impar, calcula el resultado
        else:
            resul_fila = ((fila-1)**2 + columna)
            return resul_fila
    else:
        #Verifica si la columna es mayor que la fila
        if columna % 2 == 0:
            #Si la columna es par, calcula el resultado
            resul_columna = ((columna-1)**2 + fila)
            return resul_columna
        #Si la columna es impar, calcula el resultado 
        else:
            resul_columna =(columna**2 - fila + 1)
            return resul_columna


assert number_spiral(2, 2) != 25, "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")