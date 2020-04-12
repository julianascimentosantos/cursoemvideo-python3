print('-' * 20)
print('LOJA BARATÃO'.center(20))
print('-' * 20)
soma = mais = menor = c = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    variavel = str(input('Quer continuar? [S/N] ')).upper().strip()
    soma += preço
    c += 1
    if preço > 1000:
        mais += 1
    if c == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if variavel == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {soma}')
print(f'Temos {mais} produtos custando mais de R$ 1.000.')
print(f'O produto mais barato foi {barato} que custa R$ {menor}.')

