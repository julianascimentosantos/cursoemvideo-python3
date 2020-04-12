num = int(input('Digite um número: '))
cont = 0
for n in range(1, num+1):
    if num % n == 0:
        print('\033[33m', n, end='')
        cont += 1
    else:
        print('\033[34m', n, end='')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, cont))
if cont == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO é PRIMO.')