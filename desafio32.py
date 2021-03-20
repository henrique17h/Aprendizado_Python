salario = float(input("Digite seu salário: "))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)

if salario > 1250:
    aumento = salario + (salario * 10 / 100)

print('Seu novo salário é de {:.2f}R$'.format(aumento))

