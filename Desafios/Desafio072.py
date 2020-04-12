numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'catorze', 'quize', 'dezesseis',
          'dezesete', 'dezoito','dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[num]}.')