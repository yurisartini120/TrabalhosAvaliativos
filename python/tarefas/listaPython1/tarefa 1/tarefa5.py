#Um arquivo de 15 MB, baixado a 10 Mb/s: 15 / (10/8) = 12 segundos.

wifi = int(input("Quantos Megabits(Mb/s) tem o seu wifi?"))
documento = int(input("quantos Megabytes(MB) tem o seu documento?"))


segundos = (documento / (wifi / 8))  #Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos.
print ("Tempo estimado em segundos:",segundos)


minutos = segundos / 60

print ("Tempo estimado em minutos:", minutos)



