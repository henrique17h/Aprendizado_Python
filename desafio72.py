from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
            randint(1,10), randint(1,10) )
print(f'Eu sortei os seguintes números: {numeros}',end='')
print(f'O maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')