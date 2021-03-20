letra = str(input('Digite uma frase: ')).strip().upper()
separa = letra.split()
juntar = ''.join(letra)
inverso = ''
for letra in range(len(juntar) -1, -1 , -1 ):
    inverso += juntar[letra]

if inverso == juntar:
    print('Temos um palindromo!')

else:
    print('A frase digitada não é um palindromo!')