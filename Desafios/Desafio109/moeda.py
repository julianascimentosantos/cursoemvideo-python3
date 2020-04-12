def aumentar(preço, taxa, formato=False):
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
