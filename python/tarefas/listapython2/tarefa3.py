#Faça um programa que leia 5 números e informe o maior número.

contador = 0

maior = 0


while contador < 5:
    numero = int(input("Digite um numero:"))
    contador += 1
    print(numero)

    

    if numero > maior:
        maior = numero
   

print("o maior numero é: ", maior)



    


