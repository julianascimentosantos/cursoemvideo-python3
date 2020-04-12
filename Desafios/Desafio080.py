valores = list()
for p in range(0, 5):
    n = int(input('Digite um valor: '))
    if p == 0 or n >= valores[-1]:
        valores.append(n)
        print(f'Valor adicionado ao final da lista.')
    else:
        p = 0
        while p < len(valores):
            if n <= valores[p]:
                valores.insert(p, n)
                print(f'Adicionado na {p} posição.')
                break
            p += 1
print(f'Os valores digitados foram: {valores}')