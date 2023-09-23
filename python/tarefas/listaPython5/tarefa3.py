print("contador de consoantes e vogais")

def contar_vogais():
    texto = input("Digite uma frase: ")
    vogais = 0
    consoantes = 0
    
    for letra in texto:
        if letra in vogais:
            vogais += 1

        elif letra in consoantes:
            consoantes += 1

    print(f"Vogais: {vogais}")
    print(f"Consoantes: {consoantes}")

print(contar_vogais())

