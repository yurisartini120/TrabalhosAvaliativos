'''from math import factorial
numero = int(input("Digite um numero para o Fatorial: "))
fatorial = factorial(numero)
print("o Fatorial de {} é {}".format(numero, fatorial))'''

numero = int(input("Digite um numero para o Fatorial: "))
contador = numero
fatorial = 1



# enquanto o contador foi maior que 1
while contador > 0:
   print('{}'.format(contador), end='') # imprime o contador
   print(' x ' if contador > 1 else ' = ', end='') # imprime o sinal   (se o contador for maior que 1, imprime x, senão imprime =)

   fatorial *= contador 
   contador -= 1
print("{}".format(fatorial)) # imprime o resultado fatorial   
    



