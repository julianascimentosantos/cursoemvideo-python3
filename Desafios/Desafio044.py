print('{:=^40}'.format('LOJAS NASCIMENTO'))
preço = float(input('Preço das compras R$'))
print('''Condições de pagamento: 
[ 1 ] À VISTA DINHEIRO OU CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] DIVIDIDO EM ATÉ 2X NO CARTÃO
[ 4 ] DIVIDIDO EM 3X OU MAIS NO CARTÃO''')
condição = int(input('Qual é a opção:' ))
if condição == 1:
    valor = preço - (preço * 0.10)
elif condição == 2:
    valor = preço - (preço * 0.05)
elif condição == 3:
    valor = preço
    print('Sua compra será parcelada em 2X e a parcela será de R${:.2f}.'.format(valor/2))
elif condição == 4:
    valor = preço + (preço*0.20)
    parcela = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}X e a parcela será de R${:.2f}.'.format(parcela, valor/parcela))
else:
    print('Opção não identificada, tente novamente.')
print('Sua compra de {:.2f} ficará {:.2f} no final.'.format(preço, valor))
