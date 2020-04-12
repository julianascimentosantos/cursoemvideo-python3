listanum = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor repetido, não vou adicionar...')
    cont = str(input('Quer continuar? [S/N] '))
    if cont not in 'SsNn':
        print('Opção incorreta. Tente novamente: ')
        cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'Você adicionou os valores: {sorted(listanum)}')