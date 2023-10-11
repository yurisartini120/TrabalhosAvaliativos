# Definição da classe Carro
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade} km/h")


# Obtenção dos valores de marca, modelo e ano a partir do usuário
marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano de fabricação do carro: ")

# Criação de um objeto da classe Carro com os valores fornecidos pelo usuário
meu_carro = Carro(marca, modelo, ano)

# Obtenção do valor de incremento a partir do usuário e aceleração do carro
incremento = int(input("Digite o valor de incremento para acelerar o carro: "))
meu_carro.acelerar(incremento)

# Obtenção do valor de decremento a partir do usuário e frenagem do carro
decremento = int(input("Digite o valor de decremento para frear o carro: "))
meu_carro.frear(decremento)

# Exibição das informações do carro
meu_carro.informacoes()

        
    



    
 
            

       