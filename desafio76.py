valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))

print(f'O maior valor digitado foi: {max(valores)} nas posições: ',end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...')

print(f'O menor valor digitado foi: {min(valores)} nas posições: ',end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...')
print(f'Você digitou os valores {valores}')

