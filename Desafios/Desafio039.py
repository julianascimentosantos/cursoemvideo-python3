from datetime import date
sexo = str(input('Sexo (M ou F): ').upper())
if sexo == 'M':
    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento. \nSeu alistamento será em {}.'.format(18-idade, date.today().year +(18-idade)))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos. \nSeu alistamento foi em {}.'.format(idade-18, date.today().year -(idade-18)))
    else:
        print('Você deve se alistar IMEDIATAMENTE!')
elif sexo == 'F':
    print('Você não precisa se alistar!')
else:
    print('Sexo não identificado. Tente novamente.')