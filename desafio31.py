a = int(input("Digite um número"))
b = int(input("Digite um número"))
c = int(input("Digite um número"))
maior = a
if b > a and b > c:
    maior = b

if c > b and c > a:
    maior = c

menor = a
if b < a and b < c:
    menor = b

if c < b and c < a:
    menor = c

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))

