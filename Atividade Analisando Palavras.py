#Você deve criar um programa Python que realiza as seguintes tarefas:

#1 - Solicita ao usuário que digite uma palavra.
palavra = input('Digite uma palavra: ')

#2 - Verifica se a palavra contém mais de cinco caracteres.
contagem = len(palavra)

#3 - Se a palavra tiver mais de cinco caracteres, imprima a palavra em letras maiúsculas.
#4 - Se a palavra tiver cinco ou menos caracteres, imprima a palavra em letras minúsculas.
if contagem > 5:
    print(palavra.upper())
else:
    print(palavra.lower())

#5 - Conte e imprima o número de caracteres na palavra.
print((f'A palavra tem {len(palavra)} caracteres.'))