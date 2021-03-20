valores = []
while True:
    n = int(input('Digite um número: '))

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')

    else:
        print('Valor duplicado. Digite somente números que não foram digitados! ')

    r = str(input('Quer continuar: [S/N]')).upper()[0]
    if r in 'N':
        break

valores.sort()
print(f'Você digitou os valores: {valores}')