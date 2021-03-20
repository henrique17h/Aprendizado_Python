dados = dict()
partidas = list()
dados['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantos partidas {dados["Nome"]} jogou: '))
totGols = 0
for c in range(1, total+1):
    partidas.append(int(input(f'Quantos gols na partida {c}: ')))

dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)
print(f'{dados} {totGols}')

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
    print()

print(f'O jogador {dados["Nome"]} jogou {total} partidas')
for i, v in enumerate(dados['Gols']):
    print(f'  ==> Na partida {i} fez {v} gols')
print(f'Foi um total de {dados["Total"]}')
