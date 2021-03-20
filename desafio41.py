peso = float(input('Digite seu peso:  (KG)'))
altura = float(input('Digite sua altura:  (M)'))
imc = peso /(altura ** 2)
if imc <18.5:
    print('Seu imc é de {:.1f} , e você está abaixo do peso ideal, cuidado!'.format(imc))
elif 18.5 <= imc <25:
    print('Seu imc é de {:.1f} , e você está no peso ideal'.format(imc))
elif 25 <= imc <30:
    print('Seu imc é de {:.1f} , e você está no sobrepeso'.format(imc))
elif 30 <= imc <40:
    print('Seu imc é de {:.1f} , e você está na obesidade, cuidado!'.format(imc))
elif imc >=40:
    print('Seu imc é de {:.1f} , e você está na obesidade mórbida, cuidado!!!'.format(imc))