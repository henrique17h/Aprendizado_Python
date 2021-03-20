times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atlético-GO')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros times são: {times[0: 5]}')
print('-='*15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('-='*15)
print(f'Os times em ordem são: {sorted(times)}')
print('-='*15)
print(f'A chapecoense está na : {times.index("Chapecoense")+1}º posição')