import moeda

p = float(input('Qual é o preço? R$'))
t = float(input('Qual é a taxa? (%) '))
print(f'O dobro do valor {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade do valor {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O valor {moeda.moeda(p)} aumentado em {t}% é {moeda.moeda(moeda.aumentar(p, t))}')
print(f'O valor {moeda.moeda(p)} diminuido em {t}% é {moeda.moeda(moeda.diminuir(p, t))}')
