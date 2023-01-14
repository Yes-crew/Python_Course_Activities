# Um programa que lê um número inteiro e mostre sua tabuáda

n = int(input("Digite um número para ver sua tabuada: "))

print("-" * 12)
i = 1
while i <= 10:
    print("{} x {} = {}".format(n,i,(n*i)))
    i += 1
print("-" * 12)