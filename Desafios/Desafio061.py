print('GERADOR DE PA')
print('=-' * 10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 1
while c <= 10:
    print('{} > '.format(termo), end='')
    termo += razão
    c += 1
print('FIM')
