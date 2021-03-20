soma = 0
cont = 0
num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    cont +=1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))