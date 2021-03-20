r1 = float(input('Digite o primeiro segmento do triângulo: '))
r2 = float(input('Digite o segundo segmento do triãngulo: '))
r3 = float(input('Digite o terceiro segmento do triângulo: '))

if r1 < r2 + r3 and r2< r1 + r3 and r3 < r2 + r1:
    print('Os valores digitados podem formar um triângulo!')

else:
    print('Os valores digitados não podem formar um triãngulo!')