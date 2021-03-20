velocidade= float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('Você foi multado!')
    multa= (velocidade-80) *7
print ('Você excedeu o limite de 80km e pagará {:.2f}R$ de multa'.format(multa))