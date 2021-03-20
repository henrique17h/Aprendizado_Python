print('Lojas Unic:')
preco = float(input('Digite o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10/100)
    print('Sua compra de {:.2f} vai custar R${:.2f} com 10% de desconto'.format(preco, total))
elif opcao == 2:
    total = preco -(preco * 5/100)
    print('Sua compra de {:.2f} vai custar R${:.2f} com 5% de desconto'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total /2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    parcelas = int(input('Quantas parcelas? '))
    totalParcelas = total / parcelas
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS de 20%'.format(parcelas, totalParcelas))
    print('Sua compra de R${} vai custar R${} no final.'.format(preco, total))
else:
    print('Opção inválida de pagamento. tente novamente')