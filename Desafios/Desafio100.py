from random import randint
from time import sleep


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(1, 6):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')

def somapar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


numeros = []
sorteio()
somapar()