from math import radians, cos , sin, tan
angulo= float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
print('O valor do Seno do ângulo de {}º tem o valor de {:.2f}'.format(angulo,seno))
cosseno= cos(radians(angulo))
print('O valor do Cosseno do ângulo de {}º tem o valor de {:.2f}'.format(angulo,cosseno))
tangente= tan(radians(angulo))
print('O valor da Tangente do ângulo de {}º tem o valor de {:.2f}'.format(angulo, tangente))