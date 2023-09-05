peso_peixe = float(input("quantos quilos o peixe tem? Lembrando que se passar de 50 quilos sujeito a multa!"))
limite = 50
pagar = 0


# Se o peso do peixe for menor que o limite emitido o codigo ira aparecer "peso aceitavel".


if peso_peixe < 50:
    pagar = 0
    print(peso_peixe,"peso aceitavel!!")
else:
    excesso = peso_peixe -  limite # Descobre o valor ultrapassado
    pagar = excesso * 4  #multiplica por 4

    print( peso_peixe ,"peso elevado!!" ,"valor da multa: ", pagar)





