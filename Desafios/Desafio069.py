mais18 = homens = mulheresmenos20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper().strip()
    while sexo not in 'FM':
        print('OPÇÃO ERRADA. TENTE NOVAMENTE.')
        sexo = str(input('Sexo [F/M]: '))
    print('-' * 20)
    variavel = str(input('Quer continuar? [S/N] ')).upper().strip()
    while variavel not in 'SN':
        print('OPÇÃO ERRADA TENTE NOVAMENTE.')
        variavel = str(input('Quer continuar? [S/N] ')).upper().strip()
    if idade < 18:
        mais18 +=1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    if variavel == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18} \nAo todo temos {homens} homens cadastrados. \nE temos {mulheresmenos20} mulheres com menos de 20 anos.')
