from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    print('    [ 1 ] SOMAR\n'
          '    [ 2 ] MULTIPLICAR\n'
          '    [ 3 ] MAIOR\n'
          '    [ 4 ] NOVOS NÚMEROS\n'
          '    [ 5 ] SAIR DO PROGRAMA')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        print('A soma entre {} + {} é {}.' .format(n1, n2, n1+n2))
    elif opção == 2:
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('O maior entre {} e {} é {}.'.format(n1, n2, n1))
        elif n1 < n2:
            print('O maior entre {} e {} é {}.'.format(n1, n2, n2))
        else:
            print('Os valores são iguais.')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa, volte sempre.')