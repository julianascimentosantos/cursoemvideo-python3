from random import randint
from time import sleep
pc = randint(0, 5) # computador sorteia
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) # espera 3 segundos
if jogador == pc:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}'.format(pc, jogador))