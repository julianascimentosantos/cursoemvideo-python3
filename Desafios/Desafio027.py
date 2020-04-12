nome = str(input('Digite o seu nome completo: ')).strip()
separa = nome.split()
print('Muito prazer em te conhecer! \nSeu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[len(separa)-1]))

