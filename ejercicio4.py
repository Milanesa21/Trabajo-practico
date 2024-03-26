def palindrome_reorder(palindromo):
    list_palindromos = {}
    list_resultados = []
    
    if len(palindromo) > 1 and len(palindromo) < 10**6:
        for i in palindromo:
            list_palindromos[i] = list_palindromos.get(i, 0) + 1
            

        impares = 0
        for k, v in list_palindromos.items():

            if v % 2 != 0:
                impares+= 1
                if impares > 1:
                    return "NO SOLUTION"

            if v > 2:
                list_resultados.append(k*(v//2))

            if v ==2:
                list_resultados.append(k)
                    
        for k, v in list_palindromos.items():
            if v % 2 != 0:
                list_resultados.append(k)

        for k, v in list_palindromos.items().__reversed__():
            if v % 2 == 0:
                if v > 2:
                    list_resultados.append(k*(v//2))

                if v == 2:
                    list_resultados.append(k)
                    
                if v % 2 != 0:
                    if v > 2:
                        list_resultados.append(k*(v//2))
        return "".join(list_resultados)
    else:
        return print("El palindromo debe tener una longitud mayor a 1 y menor a 10^6")


assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"