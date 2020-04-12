from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - anonasc
dados['carteira'] = int(input('Carteira de Trabalho (0 para não tem): '))
if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
