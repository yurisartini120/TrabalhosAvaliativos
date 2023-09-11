print("Candidatos")
print("------------------------------------------")
print("1- Yuri, 2-julia, 3-joão , 4-matheus.")
print("5- Voto Nulo, 6- Voto em branco")


yuri = 0
julia = 0
joao = 0
matheus = 0
nulo = 0
branco = 0

numero_de_pessoas_para_votar = int(input("quantas pessoas vão votar?"))




for i in range (numero_de_pessoas_para_votar):

    votos = input("coloque seu voto:").upper().strip()
    
    

    if votos == "1":
        yuri += 1 

    elif votos == "2":
        julia += 1

    elif votos == "3":
        joao += 1

    elif votos == "4":
        matheus += 1

    elif votos == "5":
        nulo += 1

    elif votos == "6":
        branco += 1  




percentagem_votos_nulos = ((nulo / numero_de_pessoas_para_votar) *100)
percentagem_votos_brancos = ((branco / numero_de_pessoas_para_votar) *100) 

print("yuri =", yuri)
print("julia =", julia)
print("joao =", joao)
print("matheus =", matheus)
print("votos brancos =", branco)
print("votos nulos =", nulo)        

print("percentagem de votos nulos =", percentagem_votos_nulos ,"%")
print("percentagem de votos brancos = ", percentagem_votos_brancos ,"%")
        




