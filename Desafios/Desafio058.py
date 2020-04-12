from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 a 10.\nSerá que você consegue adivinhar qual foi?')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas, PARABÉNS!!!'.format(tentativas))

