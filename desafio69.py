print('=' *15)
print('{:^15}'.format('BEM VINDO AO BANCO NEGATIVADO!!'))
print('=' *15)
valor = int(input('Digite o valor a ser sacado: '))
cedula = 50
totalCed = 0
total = valor
while True:
    if total >= cedula:
        total -= cedula
        totalCed += 1
    
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10
        
        elif cedula == 10:
             cedula = 1
        totalCed = 0
        
        if total == 0:
            break

print('Volte sempre!')