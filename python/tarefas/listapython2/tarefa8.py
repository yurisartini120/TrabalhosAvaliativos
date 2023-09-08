'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.

'''

ano_contratacao = 1995
salario_inicial = 1000.00

primeiro_aumento = 1996
aumento = 0.015


ano_atual = 2023

aumento_dobrado = 0


while primeiro_aumento < ano_atual:
    aumento_dobrado = aumento * 2


print("seu salario atual é de", aumento_dobrado)    




