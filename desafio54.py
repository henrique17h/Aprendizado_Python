somaIdade= 0
mediaIdade= 0
homemVelho = 0
nomeVelho = 0
mulher20 = 0
for pessoa in range (1, 5):
    print('======= {}º pessoa ======='.format(pessoa))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade    

    if pessoa == 1 and sexo in 'Mm':
        homemVelho = idade
        nomeVelho = nome

    if sexo in 'Mm' and idade > homemVelho:
        homemVelho = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 +=1

mediaIdade =  somaIdade / 4
print('A média das {} idades informadas é: {}'.format(pessoa, mediaIdade))
print('O homem mais velho se chama: {}'.format(nomeVelho))
print('O número de mulheres com menos 20 anos é {}'.format(mulher20))