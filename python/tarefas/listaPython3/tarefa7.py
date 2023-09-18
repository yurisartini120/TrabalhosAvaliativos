total_gasto_abonos = 0
numero_fucionarios_minimo = 0
maior_abono = 0
resultados = []

while True:
    salario = float(input("Salario (digite 0 para encerrar):"))
    if salario == 0:
        break
    
    abono = max(salario * 0.2, 100)
    
    if abono > maior_abono:
        maior_abono = 1
    
    if abono == 100:
        numero_fucionarios_minimo += 1
    
    resultados.append((salario, abono))
    total_gasto_abonos += abono
    
for salario, abono in resultados:
    print(f"Salario: R$ {salario:.2f} - abono: R$ {abono:.2f}")
    
print("\nForam processados", len(resultados),"colaboradores")
print("Total gasto com abonos: R$ {:.2f}".format(total_gasto_abonos))
print("Valor minimo pago a", numero_fucionarios_minimo, "colaboradores")
print("Maior valor de abono pago: R$ {:.2f}".format(maior_abono))                