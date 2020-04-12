from time import sleep


def valores(* num):
    maior = c = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.3)
        if c == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        c += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()