tipo_carne = input("Qual tipo de carne (File Duplo, Alcatra, Picanha)? ").strip().title()
quantidade_kg = float(input("Qual a quantidade de carne em Kg? "))

precos= {
    "File Duplo": (4.90, 5.80),
    "Alcatra": (5.90, 6.80),
    "Picanha": (6.90, 7.80)
}

if tipo_carne not in precos:
    print("Tipo invalido")
else:

    preco_por_kg = precos[tipo_carne][0] if quantidade_kg <=5 else precos [tipo_carne][1]
    preco_total = quantidade_kg * preco_por_kg

    tipo_pagamento = input("Informe o tipo de pagamento (Cartão Tabajara ou outro):").strip().title()

    if tipo_pagamento == "TABAJARA":
        desconto = 0.05 * preco_total
        preco_com_desconto = preco_total - desconto
    else:
        desconto = 0
        preco_com_desconto = preco_total

    print("Tipo de carne: ", tipo_carne)
    print("Quantidade: ", quantidade_kg)
    print("Preço total: ", preco_total)
    print("Tipo de pagamento: ", tipo_pagamento)
    print("Desconto: ", desconto)
    print("valor a pagar: ", preco_com_desconto)    