peso = float(input('Qual o peso? (kg) '))
altura = float(input('Qual a altura? (m)'))
imc = peso / (altura**2)
print('O IMC é {:.2f}'.format(imc))
