nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2
if media >=5 and media <7:
    print('Somando {:.1f} e {:.1f} a sua média é {:.1f} e você está de recuperação!'.format(nota1, nota2, media))
elif media <5:
    print('Somando {:.1f} e {:.1f} a sua média é {:.1f} e você está reprovado!'.format(nota1, nota2, media))
elif media >= 7:
    print('Somando {:1.f} e {:1.f} a sua média é {:.1f} e você está aprovado!'.format(nota1, nota2 , media))
