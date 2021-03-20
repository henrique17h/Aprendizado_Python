pessoa = dict()
grupo = list()

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: (M/F)')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Por favor digite apenas "M OU F" para sexo feminino/masculino!')
    pessoa['Idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        opc = str(input('Quer continuar: (S/N)')).upper()[0]
        if opc in 'SN':
            break
        print('Por favor digite apenas "S OU N" para continuar ou parar o programa!')

    if opc == 'N':
        break
    media = len(pessoa)
    media += pessoa['Idade']

print()
print('As mulheres cadastradas foram:')
for p in grupo:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}')

print()
print(f'As pessoas acima da média de idade:{media:5.2f} anos foram:')
for p in grupo:
    if p['Idade'] > media:
        print(f'{p["Nome"]}')

print()
print(f'Ao todo foram cadastradas {len(pessoa) + 1} pessoas.')
print(f'A média de idade de todas as pessoas as pessoas cadastradas foi {media:5.2f}')
