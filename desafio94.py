from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    print(f'iniciando a contagem de {i} até {f} contando de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
ini = int(input('Inicio da contagem: '))
fim = int(input('Final da contagem: '))
pas = int(input('Passo da contagem: '))
contador(ini, fim, pas)
