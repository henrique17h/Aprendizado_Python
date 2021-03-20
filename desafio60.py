print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo+= razao
        cont += 1
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))