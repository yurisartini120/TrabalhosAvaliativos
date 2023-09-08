'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do 
país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento'''



pais_A = 80000
taxa_crescimento_A = 0.03



pais_B = 200000
taxa_crescimento_B = 0.015

ano = 0

# Enquanto pais_A menor que pais_B
while pais_A < pais_B:
    pais_A += pais_A * taxa_crescimento_A # pais_A = pais_A + pais_A * taxa_crescimento_A
    pais_B += pais_B * taxa_crescimento_B # pais_B = pais_B + pais_B * taxa_crescimento_B
    ano += 1

print("A população do país A ultrapassou a população do país B em ", ano, "anos")









  





