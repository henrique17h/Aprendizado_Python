matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maiorL = somaP = somaC = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha , coluna}]: '))
    print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            somaP += matriz[l][c]
    print()
print(f'A soma de todos os valores pares é: {somaP}')

for l in range(0, 3):
    somaC += matriz[l][2]
print(f'A soma de todos valores da terceira coluna é: {somaC}')

for c in range(0, 3):
    if c == 0:
        maiorL = matriz[1][c]

    elif matriz[1][c]:
        maiorL = matriz[1][c]
print(f'O maior valor da segunda linha é: {maiorL}')
