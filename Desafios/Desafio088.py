from random import randint
from time import sleep
lista = []
jogo = []
print('-' * 30)
print('   JOGA NA MEGA SENA   ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
while tot <= quant:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1
for j, n in enumerate(jogo):
    print(f'Jogo {j + 1}: {n}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
