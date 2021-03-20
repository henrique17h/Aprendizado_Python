distancia = float(input('Qual a distãncia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km '.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))