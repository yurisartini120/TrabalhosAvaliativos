def validar_cpf(cpf):

    # para retirar os pontos e traços, usaremos o replace
    cpf = cpf.replace(".", "").replace("-", "")

    # agora vemos se o tamanho do cpf, é maior ou menor que 11 digitos, e se for, retornara falso, ou seja, cpf inválido
    if len(cpf) != 11:
        return False
    
    # também verificaremos se todos os numeros digitados são iguais, e se for, retornaremos falso, dnv

    if cpf == cpf[0] * 11:
        return False

    # para calcular o primeiro digito verificador, vamos fazer a multiplicação dos valores
    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito_1 = (soma * 10) % 11

    if digito_1 == 10:
        digito_1 = 0


    # e agorá, verificamos se o primeiro digito verificador está correto
    if int(cpf[9]) != digito_1:
        return False

    # e para calcular o segundo digito verificador, vamos fazer a multiplicação dos valores, com as modificações
    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito_2 = (soma * 10) % 11

    if digito_2 == 10:
        digito_2 = 0


    # e verificamos se ele está correto
    if int(cpf[10]) != digito_2:
        return False

    return True


#agora mandamos o usuário digitar o cpf, e chamar a função
cpf = input("Digite o CPF: ")
if validar_cpf(cpf):
    print("CPF válido")

else:
    print("CPF inválido")