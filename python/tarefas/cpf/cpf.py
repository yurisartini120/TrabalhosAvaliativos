#função para calcular o digito
def calcular_digito_verificador(cpf):  
    multiplicador = 10
    soma = 0
    for digit in cpf: #para cada dígito do cpf 
        soma += int(digit) * multiplicador #soma o dígito vezes o multiplicador
        multiplicador -= 1 #diminui o multiplicador
    resto = soma % 11 #calcula o resto  (soma / 11)
    if resto < 2:
        return 0 #se o resto for menor que 2 retorna 0
    else:
        return 11 - resto #se não retorna o resto
    

def verificar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "") #replace substitui o caractere
    if len(cpf) != 11 or not cpf.isdigit(): #isdigit verifica se é um número 
        #verifica se o tamanho é 11
        return False
    primeiro_digito = calcular_digito_verificador(cpf[:9])
    segundo_digito = calcular_digito_verificador(cpf[:9] + str(primeiro_digito)) 
    return cpf[-2:] == str(primeiro_digito) + str(segundo_digito)

cpf = input("Digite o CPF: ")
if verificar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")