from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua opção: '))
print('JÔ')
sleep(1)
print('KEN')
sleep(2)
print('PÔ!!!')
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
if computador == 0:#jogou pedra
    if jogador == 0:
        print('EMPATE!!!')
    
    elif jogador == 1:
        print('O jogador VENCEU!!!')
    
    elif jogador == 2:
        print('O computador VENCEU!!')
    
    else:
        print('Jogada inválida!!!')

elif computador == 1:#jogou papel
    if jogador == 0:
        print('O computador VENCEU!!!')
    
    elif jogador == 1:
        print('EMPATE')
    
    elif jogador == 2:
        print('O jogador VENCEU!!!')
    
    else:
        print('Jogada inválida!!!')

elif computador == 2:#jogou tesoura
    if jogador == 0:
        print('O jogador VENCEU!!')
    
    elif jogador == 1:
        print('O computador VENCEU!!!')
    
    elif jogador == 2:
        print('EMPATE!!!')

    else:
        print('Jogada inválida!!!')