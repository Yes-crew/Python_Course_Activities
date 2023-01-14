# Um programa que lê a altura e largura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que 
# cada litro de tinta pinta uma área de 2m^2

print("Coloque em metros a")

largura = float(input("Largura da parede: ")) 
altura = float(input("Altura da parede: "))
area = largura * altura

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(largura,altura,area))
print("Para pintar essa parede, você precisará de {}L de tinta.".format(area/2))