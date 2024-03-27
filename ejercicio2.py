
def missing_number(num, array):
    list = []
    # Crea una lista con todos los numeros desde el 1 hasta el num
    for i in range(1, num+1):
        list.append(i)
    
    #Calcula la suma de los numeros en la secuencia dada
    sum_missing = sum(array)
    #Calcula la suma de todos los numeros del 1 hasta el num
    sum_list = sum(list)
    #Calcula el numero faltante restando la suma de la secuencia dada la suma total
    resul = sum_list - sum_missing
    print(resul)
    return resul


assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")