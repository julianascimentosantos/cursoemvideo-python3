from Desafio107 import moeda

p = float(input('Qual é o preço? R$'))
t = float(input('Qual é a taxa? (%) '))
print(f'O dobro do valor {(p)} é {moeda.dobro(p)}')
print(f'A metade do valor {(p)} é {moeda.metade(p)}')
print(f'O valor {(p)} aumentado em {t}% é {moeda.aumentar(p, t)}')
print(f'O valor {(p)} diminuido em {moeda.diminuir(p, t)}')
