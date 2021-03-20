palavras = ('aprender', 'comer', 'cozinhar',
            'programar', 'dormir', 'correr',
            'malhar', 'treinar', 'descansar')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')