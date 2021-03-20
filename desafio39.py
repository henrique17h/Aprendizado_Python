from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
else:
    print('Classificalção: MASTER')