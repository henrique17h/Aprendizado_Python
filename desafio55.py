sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()
while sexo not in 'MmFf':
    sexo= str(input('Dados inválidos. por favor informe novamente seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))