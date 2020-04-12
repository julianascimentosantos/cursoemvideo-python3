somaidade = 0
maioridade = 0
mulheres = 0
nomevelho = ''
for p in range(1,5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip())
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
media = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho ))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(mulheres))
