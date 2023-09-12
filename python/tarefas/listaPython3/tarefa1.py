texto =  ["AcessorioAutomotivo"]  # 8 consoantes e 11 vogais

consoante = 0
vogais = 0

for caracter in texto[0]:
    if caracter in 'aeiou':
        vogais += 1
    else:
        consoante += 1

print(texto)
print(consoante)
print(vogais)