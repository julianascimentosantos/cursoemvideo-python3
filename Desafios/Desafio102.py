def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um numero num.
    """
    f = 1
    for n in range(num, 0, -1):
        f *= n
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


#Programa Principal
print(fatorial(4, show=True))