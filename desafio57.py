from time import sleep
n1 =  int(input('Digite um valor:'))
n2 =  int(input('Digite um valor:'))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior número 
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('Qual opção você deseja? '))

    if opcao == 1:
        soma = n1 + n2 
        print('Somando {} + {}. O resultado é: {}'.format(n1, n2, soma))
        sleep(2)
    
    elif opcao == 2:
        multiplicar = n1 * n2
        print('Multiplicando {} x {}. O resultado é: {}'.format(n1, n2, multiplicar))
        sleep(2)
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {}. O maior número é: {}'.format(n1, n2, maior))
            sleep(2)

        else:
            maior = n2
            print('Entre {} e {}. O maior número é: {}'.format(n1, n2, maior))
            sleep(2)

    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
        sleep(2)

    elif opcao == 5:
        print('Finalizando....')
        sleep(2)
print('Fim do programa!')