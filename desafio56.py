from random import randint
computador = randint(0,10)
acertou = False
palpites = 0
print('Sou seu computador... pensei em número entre 1 a 10')
print('Será que você consegue adivinhar? ')
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    
    else:
        print('Tente novamente')

print('Acertou com {} tentativas.'.format(palpites))