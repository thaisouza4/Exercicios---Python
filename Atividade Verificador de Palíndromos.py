#Crie um programa Python que verifica se uma palavra inserida pelo usuário é um palíndromo ou não. Um palíndromo é uma palavra, frase, número ou qualquer outra sequência de caracteres que se lê da mesma forma para frente e para trás, desconsiderando espaços e diferenciação entre maiúsculas e minúsculas.

# Passo 1: Entrada do Usuário
palavra = input("Digite uma palavra: ")

# Passo 2: Tratamento da Entrada
palavra = palavra.replace(" ", "").lower()

# Passo 3: Verificação de Palíndromo
e_palindromo = palavra == palavra[::-1]

# Passo 4: Saída
if e_palindromo:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
