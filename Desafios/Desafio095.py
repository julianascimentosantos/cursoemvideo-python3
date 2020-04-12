jogador = {}
partidas = []
time = []
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).upper()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, tot+1):
        partidas.append(int(input(f'  Quantos gols na partida {p}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    cont = str(input('Quer continuar? S/N '))
    if cont in 'Nn':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} -- ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  No jogo {i+1} fez {g} gols.')
    print('-' * 50)
print('VOLTE SEMPRE!')
