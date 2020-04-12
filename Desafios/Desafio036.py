casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Quantos anos para pagar? '))
prestação = casa/(anos*12)
print('O valor da prestação é {:.2f}'.format(prestação))
if prestação <= (salario*0.3):
    print('O empréstimo foi APROVADO.')
else:
    print('O empréstimo foi NEGADO.')