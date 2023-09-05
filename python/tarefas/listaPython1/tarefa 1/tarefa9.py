quantidade_morango = float(input("Quantos quilos de morangos você deseja comprar? "))
quantidade_maca = float(input("Quantos quilos de macas você deseja comprar? "))

preco_morango = 2.50   if quantidade_morango > 5 else 2.20

preco_macas = 1.80 if quantidade_maca > 5 else 1.50

valor_total = (quantidade_morango * preco_morango) + (quantidade_maca * preco_macas)

if (quantidade_morango + quantidade_maca ) > 8 or valor_total > 25:
    valor_total = valor_total * 0.9

print("O valor total a ser pago é: R$", valor_total) 
