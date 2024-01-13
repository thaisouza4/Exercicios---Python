# Crie um programa Python para calcular a média ponderada de um conjunto de notas e pesos fornecidos pelo usuário. Aqui estão as diretrizes para a atividade:

#1 - Solicite ao usuário que insira a quantidade de notas que deseja incluir na média.
qnt_numeros = int(input('Insira a quantidade de notas que deseja incluir na média (valor numerico): '))
notas = []
pesos = []
contador = 0

#2 - Para cada nota, solicite ao usuário que insira a nota e o peso correspondente.
while contador < qnt_numeros:
    nota = float(input('Insira a nota: '))
    peso = float(input('Agora insira o peso correspondente: '))
    notas.append(nota)
    pesos.append(peso)
    contador += 1

#3 - Calcule a média ponderada das notas usando a fórmula.
print(f'Essas são as notas e pesos respectivamente inseridos: {notas, pesos}.')
notasxpesos = [a * b for a, b in zip(notas, pesos)]
soma_notasxpesos = sum(notasxpesos)
soma_pesos = sum(pesos)
media = soma_notasxpesos / soma_pesos

#4 - Exiba o resultado da média ponderada.
print(f'A média ponderada das notas e pesos inseridos é: {media}.')