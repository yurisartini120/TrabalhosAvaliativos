import math

coberturo_por_litro = 6

tamanho_lata_18_litro = 18
tamanho_galao_3_6_litros = 3.6

preco_lata_18_litros = 80.00
preco_galao_3_6_litros = 25.00

area_a_ser_pintada = float(input("Informe o tamanho da area a ser pintada em metros quadrados: "))

area_a_ser_pintada *= 11.1

litros_de_tinta_necessarios = area_a_ser_pintada / coberturo_por_litro

latas_de_18_litros_necessario = math.ceil(litros_de_tinta_necessarios / tamanho_lata_18_litro)

galoes_de_3_6_litros_necessarios = math.ceil(litros_de_tinta_necessarios / tamanho_galao_3_6_litros)

latas_minimas = math.floor(litros_de_tinta_necessarios / tamanho_lata_18_litro)
litros_restantes = litros_de_tinta_necessarios - (latas_minimas * tamanho_lata_18_litro)
galoes_minimos = math.floor(litros_restantes / tamanho_galao_3_6_litros)

preco_total_latas = latas_de_18_litros_necessario * preco_lata_18_litros
preco_total_galoes = galoes_de_3_6_litros_necessarios * preco_galao_3_6_litros
preco_total_combinado = (latas_minimas * preco_lata_18_litros) + (galoes_de_3_6_litros_necessarios * preco_galao_3_6_litros)

print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas necessarias: ", latas_de_18_litros_necessario)
print("Preço total: ", preco_total_latas)

print("/n Situação 2: Comprar apenas galoes de 3,6 litros")
print("Quantidade de galoes necessarios: ", galoes_de_3_6_litros_necessarios)
print("Preço total: ", preco_total_galoes)

print("/n Situação 3: misturar latas e galoes de 3,6 litros")
print("Quantidade de latas necessarias: ", latas_minimas)
print("Quantidade de galoes necessarios: ", galoes_minimos)

print("/ n Preço total: ", preco_total_combinado)