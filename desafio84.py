from random import randint
from time import sleep

print('=-'* 30)
print('JOGA NA MEGASENA!')
print('=-'*30)
jogo = list()
sorteio = list()
quant = int(input('Quantos jogos você quer que eu sorteie: '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont+= 1

        if cont >= 6:
            break

    jogo.sort()
    sorteio.append(jogo[:])
    jogo.clear()
    total += 1
    sleep(1)

print('Resultado do sorteio:')
for i, l in enumerate(sorteio):
    print('-='*3, f'Jogo {i+1}: {l}')
print('BOA SORTE!!!')