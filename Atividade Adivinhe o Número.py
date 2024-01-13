# Objetivo: Escrever um programa em Python que gere um número aleatório e permita que o usuário tente adivinhar o número.
#Aqui estão algumas dicas para ajudá-lo a começar:
    #1. Você pode usar a biblioteca random para gerar o número aleatório.
    #2. Use um loop para permitir que o usuário faça múltiplas tentativas.
    #3. Use uma instrução condicional para verificar se a tentativa do usuário está correta.
    #4. Use uma variável para rastrear o número de tentativas.
    #5. Forneça feedback ao usuário após cada tentativa.
import random

#1. O programa deve gerar um número inteiro aleatório entre 1 e 100 (você pode usar a biblioteca random para isso).
number_aleatorio = random.randint(1, 100)

#2. O programa deve permitir que o usuário faça até 10 tentativas de adivinhar o número.
tentativas_restantes = 10

while tentativas_restantes > 0:
    number = int(input("Digite um número entre 0 e 100: "))

#3. Após cada tentativa, o programa deve fornecer uma dica dizendo se o número a ser adivinhado é maior ou menor do que o número fornecido pelo usuário.
    if number == number_aleatorio:
        print("Parabéns! Você acertou o número.")
        break
    elif number < number_aleatorio:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")

#4. O programa deve acompanhar o número de tentativas que o usuário fez.
    tentativas_restantes -= 1
    print(f"Tentativas restantes: {tentativas_restantes}")

#5. Se o usuário adivinhar o número corretamente ou usar todas as 10 tentativas, o programa deve encerrar e fornecer uma mensagem informando se o usuário ganhou ou perdeu.
    if tentativas_restantes == 0:
        print(f"Suas 10 tentativas acabaram. O número correto era {number_aleatorio}.")

#6. O programa deve ser executado até que o usuário escolha sair.