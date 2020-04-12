from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <=25:
    print('SENIOR')
else:
    print('MASTER')

