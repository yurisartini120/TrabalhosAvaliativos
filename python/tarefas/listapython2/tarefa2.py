


'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do 
país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento'''



pais_A = 80000
pais_B = 200000


crescimento_A = int((pais_A * 0.03) /100)   #24 pessoas
crescimento_B = int((pais_B * 0.015) /100)  #30 pessoas

calculo_A = pais_A + crescimento_A
calculo_B = pais_B + crescimento_B




# faça (80000 + 24) (200000 + 30) até A ser maior ou igual a B

while calculo_A <= calculo_B:
    pais_A += crescimento_A
    break
    print(pais_A)
  





