num = int(input("Digite um número inteiro: "))
print(
    """Digite a opção para conversão
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal"""
)
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("{} Convertido para BINÁRIO é: {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} Convertido para OCTAL é: {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} Convertido para Hexadecimal é: {}".format(num, hex(num)[2:]))
else:
    print("A opção digitada não é válida!!!")

