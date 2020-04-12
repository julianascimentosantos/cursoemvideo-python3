def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return f


inteiro = leiaint('Digite um número Inteiro: ')
real = leiafloat('Digite um número Real: ')
print(f'O número inteiro digitado {inteiro} e o real {real}')
