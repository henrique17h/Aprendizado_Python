total = mil = cont = menor =  0
barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: [R$]'))
    cont += 1

    if preco >= 1000:
        mil += 1
    
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        total += preco

    if resp == 'N':
        print('VOLTE SEMPRE!')
        break
    
print(f'Sua compra deu um total de: {total}R$')
print(f'{mil} Produtos custaram mais de mil reais')
print(f'O produto mais barato foi {barato} e custou {menor:.2f}R$')