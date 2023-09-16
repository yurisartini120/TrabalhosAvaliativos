
# Inicialização das variáveis
notas = []
valor = 0

# Entrada de dados
while valor != -1:
    valor = float(input("Informe uma nota (-1 para encerrar): "))
    if valor != -1:
        notas.append(valor)

# 1. Quantidade de valores lidos
quantidade_notas = len(notas)

# 2. Exibindo os valores na ordem em que foram informados
print("Valores informados:")
for nota in notas:
    print(nota, end=" ")

# 3. Exibindo os valores na ordem inversa
print("\nValores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

# 4. Calculando e mostrando a soma dos valores
soma = sum(notas)
print(f"Soma dos valores: {soma}")

# 5. Calculando e mostrando a média dos valores
media = soma / quantidade_notas
print(f"Média dos valores: {media:.2f}")

# 6. Calculando a quantidade de valores acima da média
acima_da_media = sum(1 for nota in notas if nota > media)

# 7. Calculando a quantidade de valores abaixo de sete
abaixo_de_sete = sum(1 for nota in notas if nota < 7)

print(f"Quantidade de valores acima da média: {acima_da_media}")
print(f"Quantidade de valores abaixo de sete: {abaixo_de_sete}")

# 8. Encerrando o programa
print("Programa encerrado.")
