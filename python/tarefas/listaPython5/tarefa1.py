def calcular_media(lista):
    if len(lista) == 0:
        return 0
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = []
quantidade = int(input("Quantos números você deseja adicionar à lista? "))

for i in range(quantidade):
    numero = float(input("Digite o número: "))
    numeros.append(numero)

media = calcular_media(numeros)
print(media)