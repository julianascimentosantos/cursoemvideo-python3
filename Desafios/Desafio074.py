from random import randint
sorteio = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor foi {max(sorteio)}')
print(f'O menor valor foi {min(sorteio)}')