from Desafio109 import moeda

p = float(input('Qual é o preço? R$'))
t = float(input('Qual é a taxa? (%) '))
print(f'O dobro do valor {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O valor {moeda.moeda(p)} aumentado em {t}% é {moeda.aumentar(p, t, True)}')
print(f'O valor {moeda.moeda(p)} diminuido em {t}% é {moeda.diminuir(p, t, True)}')
