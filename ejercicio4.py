def palindrome_reorder(palindromo):
    list_palindromos = {}
    list_resultados = []
    #Verifica si la longitud del palindromo cumple con el rango
    if len(palindromo) > 1 and len(palindromo) < 10**6:
        #Cuenta la frecuencia de cada caracter del palindromo y lo almacena
        for i in palindromo:
            list_palindromos[i] = list_palindromos.get(i, 0) + 1
            
        #Cuenta los impares
        impares = 0
        for k, v in list_palindromos.items():
            #Si es impar, incrementa el contador
            if v % 2 != 0:
                impares+= 1
                #Si hay mas de un caracter imoar, returna un NO SOLUTION
                if impares > 1:
                    return "NO SOLUTION"
            #Si el caracter es mayor a 2, agrega la mitad a la lista de resultados
            if v > 2:
                list_resultados.append(k*(v//2))

            # Si el caracter es igual a 2, agrega uno de ellos a la lista de resultados
            if v == 2:
                list_resultados.append(k)
        #Agrega los caracteres impares a la lista de resultados
        for k, v in list_palindromos.items():
            if v % 2 != 0:
                list_resultados.append(k)

        #Agrega la otra mitad de los caracteres que esten mas de 2 veces a la lista de resultados
        for k, v in list_palindromos.items().__reversed__():
            if v % 2 == 0:
                if v > 2:
                    list_resultados.append(k*(v//2))

                if v == 2:
                    list_resultados.append(k)
                    
            if v % 2 != 0:
                if v > 2:
                    list_resultados.append(k*(v//2))
        # Convierte la lista de caracteres resultantes en una cadena y la retorna
        return "".join(list_resultados)
    else:
        return print("El palindromo debe tener una longitud mayor a 1 y menor a 10^6")


assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"