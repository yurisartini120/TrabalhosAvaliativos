'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.

'''


salario_inicial = float(input("DIgite seu salario inicial"))


aumento = 0.015

ano_atual = 2023


for ano in range(ano_atual - 1996):

    aumento *= 2
    salario_atual = salario_inicial + salario_inicial * aumento

print(f"Salario atual do funcionario: {salario_atual:.2f}")

