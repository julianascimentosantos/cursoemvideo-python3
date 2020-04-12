pessoas = {}
dados = []
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).upper()
    pessoas['sexo'] = str(input('Sexo: ')).upper()[0]
    if pessoas['sexo'] not in 'FfMm':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    pessoas.clear()
    cont = str(input('Quer continuar? S/N '))
    if cont not in 'SsNn':
        print('ERRO! Por favor, digite apenas S ou N.')
        cont = str(input('Quer continuar? S/N '))
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} cadastradas.')
media = soma / len(dados)
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in dados:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO. >>')