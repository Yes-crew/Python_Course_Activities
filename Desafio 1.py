# Script que diz "Olá [nome]! Prazer em te conhecer!" em que nome tem que ser colocado pelo usuário no terminal

nome = input("Qual o seu nome? ")

#print("Olá", nome+"! Prazer em te conhecer!")
print("É um prazer te conhecer {:=^20}!".format(nome))
