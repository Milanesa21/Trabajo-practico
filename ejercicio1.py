numero = int(input("Digite um número: "))

def weird_algorithm(numero):
    list=[]
    
    # Verifica que el numero este en el rango permitido
    if numero > 1 and numero < 10**6:
        list.append(numero)
        
        #Mientras el numero no sea igual a 1, se continua aplicando el algoritmo
        while numero != 1:
            # Si el numero es par, se divide por 2
            if numero % 2 == 0:
                numero = numero // 2
                list.append(numero)
            # Si es impar, se multiplica por 3 y se suma 1
            else:
                numero = (3 * numero) + 1
                list.append(numero)
    
    return list

test = weird_algorithm(numero)
print(test)

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")