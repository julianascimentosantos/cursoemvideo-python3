n = c = s = 0
while n != 999:
    n = float(input('Digite um número [999 para parar]: '))
    s += n
    c += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(c-1, s-999))