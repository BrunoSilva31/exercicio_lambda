numeros = [num for num in range(1, 11)]

# Retornar somente os pares usando filter
numeros_pares = list(filter(lambda pares: pares % 2 == 0, numeros))
print(numeros_pares)


# Retornar somente os ímpares usando filter
numeros_impares = list(filter(lambda impares: impares % 2 != 0, numeros))
print(numeros_impares)


# Retornar somente numeros maiores que 5
maior = list(filter(lambda num: num > 5, numeros))
print(maior)


# Apenas as meninas da lista
nomes = [('Rafaela', 'F'), ('João', 'M'), ('Pedro', 'M'), ('Ariel', 'M')]

meninas = list(filter(lambda valor: valor[1] == 'F', nomes))
meninas = list(map(lambda valor: valor[0], meninas))[0]
print(meninas)
