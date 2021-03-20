# Esse programa tem como fazer melhor com condicionais. A frente terá com condicionais

num = int(input('Digite um número:'))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10

print('A unidade do seu número é: {}'.format(u))
print('A dezena do seu número é: {}'.format(d))
print('A centena do seu número é: {}'.format(c))
print('O milhar do seu número é: {}'.format(m))