# Exercício 5: Filtragem de Dicionário

'''
Dado um dicionário de informações de alunos, escreva um programa que
filtre os alunos que têm uma nota superior a 85 e crie um novo dicionário
com esses alunos.
'''


alunos = {
    "julia": 85,
    "amanda":90,
    "yuri": 45,
    "samantha": 86
}
print(alunos)

aprovados = {}

for nomes, notas in alunos.items():
    if notas >= 85:
        aprovados[nomes]= notas
    
print(aprovados)
        
        