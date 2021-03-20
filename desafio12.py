salario= float(input('Qual é o valor do funcionário do funcionário? RS'))
novo = salario + (salario * 15 / 100)
print ('Um funcionário que ganhava RS {:.2f}, com 15%  de aumento, passa a receber RS{:.2f}'.format(salario, novo))