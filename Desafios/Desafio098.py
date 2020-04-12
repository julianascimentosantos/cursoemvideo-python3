from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)

    c = i
    if i < f:
        while c <= f:
            print(f'{c}', end=' ')
            c += p
            sleep(0.5)
    else:
        while c > f:
            print(f'{c}', end=' ')
            c -= p
            sleep(0.5)
    print('FIM!')


#Programa principal
cont(1, 10, 1)
cont(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)