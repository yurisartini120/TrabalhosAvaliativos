'''Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o
resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada
dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores
referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido
completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e
informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:'''

# Inicialize um vetor para armazenar os votos de cada sistema operacional
votos = [0, 0, 0, 0, 0, 0]

# Variável para contar o total de votos
total_votos = 0

# Solicita que o usuário insira os votos até que 0 seja inserido
while True:
    print("Escolha o sistema operacional (1 - Windows Server, 2 - Unix, 3 - Linux, 4 - Netware, 5 - Mac OS, 6 - Outro): ")
    voto = int(input())
    
    # Verifica se o voto é válido (entre 1 e 6)
    if voto < 0 or voto > 6:
        print("Voto inválido. Por favor, insira um valor entre 1 e 6.")
        continue
    
    # Se o voto for 0, encerra a entrada de dados
    if voto == 0:
        break
    
    # Incrementa o contador de votos para o sistema operacional correspondente
    votos[voto - 1] += 1
    total_votos += 1

# Imprime o cabeçalho da tabela
print("\nSistema Operacional  Votos     %")
print("-------------------  -----  -----")

# Define uma lista de nomes de sistemas operacionais
sistemas_operacionais = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

# Variáveis para acompanhar o sistema operacional mais votado e sua porcentagem
vencedor = ""
mais_votos = 0

# Imprime os votos para cada sistema operacional
for i in range(6):
    percentual = (votos[i] / total_votos) * 100
    print(f"{sistemas_operacionais[i]:<20} {votos[i]:<6} {percentual:.2f}%")
    
    # Verifica se este é o sistema operacional mais votado até agora
    if votos[i] > mais_votos:
        mais_votos = votos[i]
        vencedor = sistemas_operacionais[i]

# Imprime o total de votos
print("-------------------  -----")
print(f"Total                {total_votos}\n")

# Imprime o sistema operacional vencedor
print(f"O Sistema Operacional mais votado foi o {vencedor}, com {mais_votos} votos, correspondendo a {((mais_votos / total_votos) * 100):.2f}% dos votos.")
