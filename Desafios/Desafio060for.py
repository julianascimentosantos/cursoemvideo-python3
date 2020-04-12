n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = '.format(n), end='')
f = 1
for m in range (n, 0, -1):
    print('{}'.format(m), end='')
    print(' x ' if m > 1 else ' = ', end='')
    f *= m
print('{}'.format(f))