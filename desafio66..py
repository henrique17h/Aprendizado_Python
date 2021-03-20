from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''   
    while tipo not in 'PI':
        tipo = str(input('Par ou impar: [P/I]')).strip().upper()    
    print(f'Você jogou {jogador} e o computador {computador}. E o total foi: {total}', end='')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
       if total % 2 == 0:
            print('Você venceu')
            v += 1
        
        
    else:
        print('Você perdeu')
        break   
        
        elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
    
        else:
            print('Você perdeu')
            break
print(f'Você ganhou {v} consecutivas ')
    
