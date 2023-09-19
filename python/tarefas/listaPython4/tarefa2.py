'''
Crie um programa que solicita ao usuário que insira as notas de um aluno em
diferentes disciplinas. Armazene essas notas em uma tupla.
Em seguida, calcule a média das notas e informe ao usuário
'''

portugues = float(input("coloque sua nota de portugues: "))
ingles = float(input("coloque sua nota de ingles: "))
matematica = float(input("coloque sua nota de matematica: "))
fisica = float(input("coloque sua nota de fisica: "))
biologia = float(input("coloque sua nota de biologia: "))

nota = [portugues, matematica, fisica, biologia, ingles]
media = [(portugues+ matematica+ fisica+ biologia + ingles) /(len(nota))]

print(media)



   
 
    
        
    
    
    






