casa = float(input("Qual o valor da casa a ser financiada? "))
salario = float(input("Qual o teu salário mensal? "))
anos = float(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa no valor de {:.2f} em {} anos".format(casa, anos), end='')
print("A prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print('O empréstimo pode ser concedido!')
else:
    print('O empréstimo não pode ser concedido')