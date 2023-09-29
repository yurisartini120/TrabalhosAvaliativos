#Exercício 4: Dicionário de Dicionários

'''
Modifique o exercício anterior para criar um dicionário de dicionários,
onde cada aluno é representado por um dicionário contendo idade e
nota.
'''


dados_alunos ={
    "yuri" : {'idade' : 17, 'nota' : 90},
    "julia" : {'idade' : 19, 'nota' : 100}
}

for item in dados_alunos.items():


    print(item)