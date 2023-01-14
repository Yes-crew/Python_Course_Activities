# Um programa que lê quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

n = float(input("Quanto dinheiro você tem na carteira? R$"))

print("Com R${} você pode comprar US${:.2f}".format(n, n/5.17))
