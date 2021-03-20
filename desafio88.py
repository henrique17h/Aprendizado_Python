from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Digite seu nome: '))
nasc = int(input('Digite o seu ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Número da carteira de trabalho(0: caso não tenha CTPS): '))

if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano da contratação: '))
    dados['Sálario'] = float(input('Digite o seu salário: '))
    dados['Aposentadoria'] = dados['Idade']+((dados['Contratação']+35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} = {v}')
