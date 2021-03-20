num = (int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3)+1}º posição')
else:
    print(f'O número 3 não foi digitado')
for n in num:
    if n % 2 == 0:
        print(n, end='')