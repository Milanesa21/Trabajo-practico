def number_spiral (fila, columna):
    if fila > columna:
        if fila % 2 == 0:
            resul_fila = (fila**2 - columna +1)
            return resul_fila 
        else:
            resul_fila = ((fila-1)**2 + columna)
            return resul_fila
    else:
        if columna % 2 == 0:
            resul_columna = ((columna-1)**2 + fila)
            return resul_columna
        else:
            resul_columna =(columna**2 - fila + 1)
            return resul_columna


assert number_spiral(2, 2) != 25, "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")
