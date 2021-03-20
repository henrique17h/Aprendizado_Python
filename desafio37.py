from datetime import date

nascimento = int(input("Digite o ano de nascimento: "))
atual = date.today().year
idade = atual - nascimento
if idade == 18:
    print("Você tem {} anos e deve se alistar neste ano ".format(idade))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(
        "Você tem {} anos e já se foram {} anos do seu alistamento".format(idade, saldo)
    )
    print("O seu ano de alistamento era no ano de {}".format(ano))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(
        "Você tem {} anos e faltam {} anos para o seu alistamento".format(idade, saldo)
    )
    print("O seu ano de alistamento será no ano de {}".format(ano))
