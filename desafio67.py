totH = tot20 = tot18  = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
        
    if sexo == 'M':
            totH += 1
        
    if idade > 18:
            tot18 += 1
        
    if sexo == 'F' and idade < 20:
            tot20 +=1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':
        break

print(f'Foram cadastrados {tot18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {totH} Homens')
print(f'Foram cadastradas {tot20} mulheres menos de 20.')
