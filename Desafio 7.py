# Um programa que lê as duas notas de um aluno, calcula e mostre sua média.

n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
n3 = (n1 + n2) / 2

print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1,n2,n3))