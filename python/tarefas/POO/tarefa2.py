import time

nota = []

class estudante:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def adicionar_nota(self, nota):
        self.nota.append(nota)

    def calcular_media(self):
        return sum(self.nota) / len(self.nota)


nome = input("Digite o nome do estudante: ")
time.sleep(0.5)

matricula = input("Digite a matricula do estudante: ")
time.sleep(0.5)

print("Para encerrar digite -1")
time.sleep(0.5)

estudante_obj = estudante(nome, matricula, nota)

notas = float(input("Digite a nota do estudante: "))
nota.append(notas)
estudante_obj.adicionar_nota(notas)

while notas != -1:
    notas = float(input("Digite a nota do estudante: "))
    if notas != -1:
        nota.append(notas)
        estudante_obj.adicionar_nota(notas)

media = estudante_obj.calcular_media()

print(f"Nome: {estudante_obj.nome}")
print(f"Matricula: {estudante_obj.matricula}")
print(f"Notas: {estudante_obj.nota}")
print(f"Media: {media}")