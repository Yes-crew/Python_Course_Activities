# Faça um algoritmo que leia o salário de um funcionário

n1 = float(input("Qual o salário do funcionário? R$"))
n2 = n1 + (n1 * 15 / 100)

print("Um funcionário que ganhava R${:.2f}, com um aumento de 15%, passa a receber R${:.2f}".format(n1,n2))
