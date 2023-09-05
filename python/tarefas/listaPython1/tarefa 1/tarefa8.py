gasolina = 2.50
alcool = 1.95

litros_vendidos = float(input("Quantos litros foram vendidos? "))
tipo_combustivel = input("Tipo de combustivel: (A-álcool, G-gasolina)").strip().upper()


if tipo_combustivel == "A":
  if litros_vendidos > 20:
        valor = litros_vendidos * (alcool - (alcool * 0.03))
  else:
        valor = litros_vendidos * (alcool - (alcool * 0.05))
   

elif tipo_combustivel == "G":
     if litros_vendidos <= 20:
        valor = litros_vendidos * (gasolina - (gasolina * 0.04))
     else:
        valor = litros_vendidos * (gasolina - (gasolina * 0.06))

else:
    print("Tipo de combustivel invalido, Coloque 'A' ou 'G'")
    valor = 0

if valor > 0:
    print("Valor total: R$", valor)       




