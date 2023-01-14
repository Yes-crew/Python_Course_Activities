# Um algorítimo que lê o preço de um produto e mostra seu novo preço, com 5% de descoto

n1 = float(input("Qual é o preço do produto? R$"))
n2 = n1 - (n1 * 5 / 100)

print("O preço do produto que custava {}, na promoção com desconto de 5% vai custar R${:.2f}".format(n1,n2))