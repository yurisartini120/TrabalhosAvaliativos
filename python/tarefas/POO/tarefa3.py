import time

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            time.sleep(0.5)
            print("Livro emprestado com sucesso!")
        else:
            time.sleep(0.5)
            print("O livro não está disponível para empréstimo.")
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            time.sleep(0.5)
            print("Livro devolvido com sucesso!")
        else:
            time.sleep(0.5)
            print("O livro já está disponível.")

# Criar objetos da classe Livro
livro1 = Livro("Moby Dick", " Herman Melville", 1851)
livro2 = Livro("O poder da esperança", "Michelson Borges", 2018)

# Exibir livros disponíveis
def exibir_livros_disponiveis():
    print("Livros disponíveis:")
    if livro1.disponivel:
        time.sleep(0.5)
        print("1. " + livro1.titulo)
    if livro2.disponivel:
        time.sleep(0.5)
        print("2. " + livro2.titulo)

# Menu interativo para emprestar e devolver livros
while True:
    print("===== MENU =====")
    print("1. Emprestar livro")
    print("2. Devolver livro")
    print("3. Exibir livros disponíveis")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    time.sleep(0.5)
    
    if opcao == "1":
        exibir_livros_disponiveis()
        
        escolha = input("Escolha o número do livro que deseja emprestar: ")
        
        if escolha == "1":
            livro1.emprestar()
        elif escolha == "2":
            livro2.emprestar()
        else:
            print("Opção inválida!")
    
    elif opcao == "2":
        print("Livros emprestados:")
        
        if not livro1.disponivel:
            time.sleep(0.5)
            print("1. " + livro1.titulo)
        if not livro2.disponivel:
            time.sleep(0.5)
            print("2. " + livro2.titulo)
        
        escolha = input("Escolha o número do livro que deseja devolver: ")
        
        if escolha == "1":
            livro1.devolver()
        elif escolha == "2":
            livro2.devolver()
        else:
            print("Opção inválida!")
    
    elif opcao == "3":
        exibir_livros_disponiveis()
    
    elif opcao == "4":
        time.sleep(0.5)
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida!")