matrizes = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrizes[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matrizes[l][c] % 2 == 0:
            pares += matrizes[l][c]
        soma += matrizes[l][2]
        maior = matrizes[1][0] or maior < matrizes[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrizes[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da ultima coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
