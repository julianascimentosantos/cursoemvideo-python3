soma = c = menor = maior = 0
continuar = 'S'
while continuar in 'sS':
    n = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    while continuar not in 'SN':
        print('TENTE NOVAMENTE')
        continuar = str(input('Deseja continuar [S/N] ')).upper().strip()
print('Você digitou {} números e a média foi {:.2f}.'.format(c, soma/c))
print(f'O maior valor foi {maior} e o menor foi {menor}.')
