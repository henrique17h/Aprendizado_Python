boletim = list()

while True:
    nome = str(input('Digite o seu nome: '))
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digita a 2º nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    resp = str(input('Deseja continuar: (S/N)'))
    if resp in 'Nn':
        break

print()
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(boletim):
    print(f'{i:<4} {a[0]:<10}  {a[2]:>5.1f}')
print()

while True:
    opc = int(input('Qual aluno você deseja ver o boletim: ("999"INTERROMPE)'))
    if opc == 999:
        break

    if opc <= len(boletim):
        print(f'Notas de {boletim[opc][0]}, são {boletim[opc][1]}')
print()
print('Volte Sempre!!!')