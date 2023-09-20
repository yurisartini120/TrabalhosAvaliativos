import random


faces_do_dado = (1, 2, 3, 4, 5, 6)

input("Pressione Enter para lançar o dado...")

# Gerar um número aleatório entre 1 e 6
numero_aleatorio = random.choice(faces_do_dado)

# Pedir ao usuário para escolher um número

numero_escolhido = int(input("Escolha um número entre 1 e 6: "))

# Verificar se o número escolhido pelo usuário corresponde ao número gerado aleatoriamente

if numero_escolhido in faces_do_dado:
    
    if numero_escolhido == numero_aleatorio:
        
        print(f"Você ganhou! O número {numero_aleatorio} corresponde ao número gerado.")
    else:

        print(f"Você perdeu! O número gerado foi {numero_aleatorio}.")
else:

    print("Por favor, escolha um número válido entre 1 e 6.")