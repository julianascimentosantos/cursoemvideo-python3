def aumentar(preço, taxa, formato=False):
    """

    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço, taxa, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    """
    -> Resumo dos dados (aumento e redução de uma percentagem, dobro e metade do valor)
    preço: valor base para o resumo
    taxaa: taxa para aumento
    taxar: taxa para redução
    """
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)

