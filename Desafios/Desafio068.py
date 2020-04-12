from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = ' '
    v = 0
    #while tipo not in 'PI':
    tipo = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total}.')
    print('-' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU.')
            v += 1
        else:
            print('Você PERDEU.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU.')
            v += 1
        else:
            print('Você PERDEU.')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes')


