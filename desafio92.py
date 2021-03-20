print('Controle de terrenos')
print('-' * 30)


def area(largura, comprimeto):
    resultado = largura * comprimeto
    print(f'A área de um terreno de {largura}x{comprimeto} é de {resultado}m')


la = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
print(area(la, c))



