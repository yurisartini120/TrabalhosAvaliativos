print("contador de consoantes e vogais")
print("------------------------------")
texto = input("Digite uma palavra para contarmos as vogais e consoantes: ") .lower()
consoante = 0
vogais = 0
print("------------------------------")
def contar_vogais(texto, consoante, vogais):
    
    for caracter in texto:
        if caracter in 'aeiou':
            vogais += 1
        else:
            consoante += 1

    print(texto)
    print("consoantes:",consoante)
    print("vogais:",vogais)

print(contar_vogais(texto, consoante, vogais))

