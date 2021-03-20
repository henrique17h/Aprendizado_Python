from math import hypot
co= float(input('Digite o valor do cateto oposto:'))
ca= float(input('Digite o valor do cateto adjacente'))
h1 = hypot(ca, co)
print('O valor da hipotenusa é: {:.2f}'.format(h1))