print ("CRIME EM ANDAMENTO")
print ("RESPONDA COM SIM OU NAO")

veredito = 0

if input("você telefonou para a vitima?") == "sim":
  veredito = veredito + 1
if input("esteve no local do crime?") == "sim":
  veredito = veredito + 1
if input("mora perto da vitima?") == "sim":
  veredito = veredito + 1
if input("devia para a vitima?") == "sim":
  veredito = veredito + 1
if input("ja trabalhou com a vitima?") == "sim":
  veredito = veredito + 1


if veredito <= 2:
  print("SUSPEITO")
elif veredito <= 4:
  print("CÚMPLICE")
elif veredito == 5:
  print("ASSASSINO")
else:
  print("INOCENTE")  
  