import tkinter as tk

 

def calcular_classificacao():

    respostas_positivas = 0

 

    resposta1 = entry_resposta1.get().strip().lower()

    if resposta1 == "sim":

        respostas_positivas += 1

 

    resposta2 = entry_resposta2.get().strip().lower()

    if resposta2 == "sim":

        respostas_positivas += 1

 

    resposta3 = entry_resposta3.get().strip().lower()

    if resposta3 == "sim":

        respostas_positivas += 1

 

    resposta4 = entry_resposta4.get().strip().lower()

    if resposta4 == "sim":

        respostas_positivas += 1

 

    resposta5 = entry_resposta5.get().strip().lower()

    if resposta5 == "sim":

        respostas_positivas += 1

 

    if respostas_positivas == 2:

        resultado_label.config(text="Classificação: Suspeita")

    elif 3 <= respostas_positivas <= 4:

        resultado_label.config(text="Classificação: Cúmplice")

    elif respostas_positivas == 5:

        resultado_label.config(text="Classificação: Assassino")

    else:

        resultado_label.config(text="Classificação: Inocente")

 

# Cria a janela

window = tk.Tk()

window.title("Classificação de Suspeição")

window.geometry("400x300")

window.configure(bg="#a0a0a0")

 

# primeira pergunta

pergunta1_label = tk.Label(window, text="Telefonou para a vítima?", bg="#a0a0a0", fg="white")

pergunta1_label.pack(pady=5)

 

entry_resposta1 = tk.Entry(window)

entry_resposta1.pack()

 

# segunda pergunta

pergunta2_label = tk.Label(window, text="Esteve no local do crime?", bg="#a0a0a0", fg="white")

pergunta2_label.pack(pady=5)

 

entry_resposta2 = tk.Entry(window)

entry_resposta2.pack()

 

# terceira pergunta

pergunta3_label = tk.Label(window, text="Mora perto da vítima?", bg="#a0a0a0", fg="white")

pergunta3_label.pack(pady=5)

 

entry_resposta3 = tk.Entry(window)

entry_resposta3.pack()

 

# quarta pergunta

pergunta4_label = tk.Label(window, text="Devia para a vítima?", bg="#a0a0a0", fg="white")

pergunta4_label.pack(pady=5)

 

entry_resposta4 = tk.Entry(window)

entry_resposta4.pack()

 

# quinta pergunta

pergunta5_label = tk.Label(window, text="Já trabalhou com a vítima?", bg="#a0a0a0", fg="white")

pergunta5_label.pack(pady=5)

 

entry_resposta5 = tk.Entry(window)

entry_resposta5.pack()

 

# Botão

calcular_button = tk.Button(window, text="Calcular Classificação", command=calcular_classificacao, bg="#a0a0a0", fg="white")

calcular_button.pack(pady=10)

 

 

resultado_label = tk.Label(window, text="", bg="#a0a0a0", fg="white")

resultado_label.pack()

 

# Inicia a janela

window.mainloop()