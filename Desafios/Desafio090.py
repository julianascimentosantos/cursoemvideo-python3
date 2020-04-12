aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
elif 5 < aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')