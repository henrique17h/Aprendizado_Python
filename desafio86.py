aluno = {}
situacao = []

aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input('Digite sua média: '))

if aluno['media'] <= 5:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print('-='* 30)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')