from random import randint
from time import sleep
computador= randint(0,5)#faz o computador esperar
print('===#===' *20)
print('Vou pensar em un número entre 0 e 5 tente adivinhar...')
print('===#===' *20)
jogador= int(input('Em que número pensei? '))#jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER -.-')
else:
    print('Ganhei eu pensei no número {} e não no {}'.format(computador, jogador))