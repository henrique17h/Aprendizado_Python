temp =  []
princ = []
cont = 0
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append((float(input('Peso: '))))

    if len(princ) == 0:
        maior = menor = temp[1]

    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resposta = str(input('Deseja continuar: S/N'))
    cont += 1

    if resposta in 'Nn':
        break


print(princ)
print(f'Foram cadastradas {cont} pessoas')
print(f'O maior peso foi de: {maior}KG. Peso de: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'O menor peso foi de {menor}KG. Peso de: ', end='')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end='')