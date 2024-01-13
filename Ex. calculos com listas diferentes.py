lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

# Soma de elementos correspondentes
soma_resultado = [a + b for a, b in zip(lista1, lista2)]
print(f"Soma dos elementos correspondentes: {soma_resultado}")
