viagem = float(input('Qual é a distância da viagem? '))
'''if viagem < 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45'''
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('O valor da sua viagem é {:.2f}'.format(preço))
