produtos = ('Lápis', 'Borracha', 'Caderno', 'Estojo',
            'Transferidor', 'Compasso', 'Mochila',
            'Canetas', 'Livro')
preços = (1.75, 2, 15.9, 25, 4.2, 9.99,
          120.32, 22.3, 34.9)
for pos in range(0, len(produtos)):
    print(produtos[pos], '.' * 30, 'R$', preços[pos])