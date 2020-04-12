n1 = float(input("Primeira nota: "))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('REPROVADO')
elif 5 <= media < 6.9:
    print('RECUPERAÇÃO')
elif 10 >= media > 7:
    print('APROVADO')
else:
    print('ERRO! As notas só podem estar entre 0 e 10. Tente novamente.')
