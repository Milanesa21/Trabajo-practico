numero = int(input("Digite um número: "))

def weird_algorithm(numero):
    list=[]
    if numero > 1 and numero < 10**6:
        list.append(numero)
        while numero != 1:
            if numero % 2 == 0:
                numero = numero // 2
                list.append(numero)
                
            else:
                numero = (3 * numero) + 1
                list.append(numero)
        
    return list

test = weird_algorithm(numero)
print(test)

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")