from time import sleep

time = list()
dados = dict()
partidas = list()

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantos partidas {dados["Nome"]} jogou: '))
    partidas.clear()
    totGols = 0

    for c in range(1, total+1):
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))

    dados['Gols'] = partidas[:]
    dados['Total'] = sum(partidas)
    time.append(dados.copy())

    while True:
        resp = str(input('Quer continuar: (S/N)')).upper()[0]
        if resp in 'SN':
            break
        print('Por favor digite apenas "S/N" para continuar ou parar o programa')
    if resp == 'N':
        break
    sleep(1)

print('-=' * 30)
print('Cod', end='')

for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

while True:
    busca = int(input('Deseja ver os dados de qual jogador: (999 para interromper)'))
    if busca == 999:
        break

    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código: {busca}!')
        sleep(1)

    else:
        print(f' ----- Levantamento do Jogador {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'      No jogo {i+1} fez {g} gols.')
    print('-=' * 40)
sleep(2)
print('<<<< VOLTE SEMPE!!! >>>>')
