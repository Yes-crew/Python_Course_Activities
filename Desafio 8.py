# Um programa que lê um valor em metros e exiba o valor convertido em km, hm, dam, dm, cm, mm

n = float(input("Uma distância em metros: "))

print("A medida de {}m corresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm".format(n,(n/1000),(n/100),(n/10),(n*10),(n*100),(n*1000)))
