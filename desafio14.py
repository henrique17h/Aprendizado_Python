percorrido = float(input('Qual a quantidade de km percorridos?'))
dias = int(input('Quantos dias alugado?'))
pago = (dias * 60) + (percorrido *0.15)

print('O total a se pagar é de R$:{:.2f}'.format(pago))