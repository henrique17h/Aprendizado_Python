cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número entre 0 a 10: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end='')
print(f'você digitou {num} que por extenso é {cont[]}')