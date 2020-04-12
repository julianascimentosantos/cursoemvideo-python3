soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        #soma = soma + n
        soma += n
        #cont = cont + 1
        cont += 1
print('A SOMA É {} E A QUANTIDADE {}.'.format(soma, cont))