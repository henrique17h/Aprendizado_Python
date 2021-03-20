lista = ('Mochila', 120.99,
         'Lápis', 1.50,
         'Borracha', 1.00,
         'Caderno', 7.99,
         'Estojo', 6.50,
         'Régua', 4.50,
         'Portifólio', 11.99)
print('-'*40)
print(f'{"Listagem de preços":^40}')
print('-'*40)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    
    else: 
        print(f'R${lista[pos]:>5.2F}')
    