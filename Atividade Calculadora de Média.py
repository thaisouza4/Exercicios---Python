#Crie um programa em Python para calcular a média de um conjunto de números fornecidos pelo usuário. Aqui estão as diretrizes:

#1 - Solicite ao usuário que insira quantos números deseja incluir na média.
qnt_numeros = int(input('Insira quantos números deseja incluir na média (valor em formato númerico): '))
entradas = []
contador = 0

#2 - Em seguida, peça ao usuário que insira cada número individualmente.
while contador < qnt_numeros:
    entrada = float(input('Insira cada número individualmente: '))
    entradas.append(entrada)
    contador += 1

#3 - Calcule a média dos números fornecidos.
print(entradas)
soma = sum(entradas)
media = soma / qnt_numeros

#4 - Exiba o resultado da média.
print(f'A média dos números inseridos é: {media}')