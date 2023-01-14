# Calcular o quanto deve ser pago por alugar um carro

days = float(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

total_price = (60 * days) + (0.15 * km)

print("O total a pagar é de R${:.2f}".format(total_price))