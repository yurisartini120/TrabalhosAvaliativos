# Solicita o valor do salário por hora e o número de horas trabalhadas
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas

# Calcula os descontos
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto

# Calcula o salário líquido
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

# Exibe os resultados
print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (11%) : R$ {imposto_renda:.2f}")
print(f"- INSS (8%) : R$ {inss:.2f}")
print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")
