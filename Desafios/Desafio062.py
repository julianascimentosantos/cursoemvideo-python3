print('GERADOR DE PA')
print('=-' * 10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} > '.format(termo), end='')
        termo += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
