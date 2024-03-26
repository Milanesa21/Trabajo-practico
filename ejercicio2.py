
def missing_number(num, array):
    list = []
    for i in range(1, num+1):
        list.append(i)
        
    sum_missing = sum(array)
    sum_list = sum(list)
    resul = sum_list - sum_missing
    print(resul)
    return resul


assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")