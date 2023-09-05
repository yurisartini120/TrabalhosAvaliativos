numero1 = int(input("coloque o 1° valor: "))
numero2 = int(input("coloque o 2° valor: "))


operação = input("Qual operação matematica deseja realizar? + - * /")

if operação == "+":
    resultado = numero1 + numero2
    print(resultado)

elif operação == "-":
    resultado = numero1 - numero2   
    print(resultado)
    
elif operação == "*":
    resultado = numero1 * numero2
    print(resultado)
    
elif operação == "/":
    resultado = numero1 / numero2
    print(resultado)
else:
    print("coloque algo")


if resultado < 0:
    print("Este numero é negativo")
else:
    print("Este numero é positivo")    



if "." in str(resultado):
    print("o numero é decimal") 
else:
    print("o numero é inteiro")  



if resultado % 2 == 0:
    print ("numero é par")
else:
    print ("numero é impar")