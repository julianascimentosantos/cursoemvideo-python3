'''valores = []
pares = []
impares = []
for v in range(1, 8):
    valores.append(int(input(f'Digite o {v}º valor: ')))
for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)'''
num = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')