'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.

'''
dias = int(input("quer medir a temepratura de quantos dias?"))

contador = 0
soma = 0
maior = 0
menor = 0




while contador < dias:
    temperatura = int(input("informe a temperatura:"))
    contador += 1
    print(temperatura)

    soma = soma + temperatura

    if temperatura > maior:
        maior = temperatura
    elif menor < maior:
        menor = temperatura    
    

media = float(soma / dias)



print ("a temperatua maior foi de", maior, "°")
print("a temepratura menor foi de", menor, "°")
print("a media das temperaturas foi de {:.1f} °".format(media))






