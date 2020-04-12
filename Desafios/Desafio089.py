ficha = []
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    cont = str(input('Quer continuar? S/N '))
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<8}{"NOME":<15}{"MÉDIA":>3}')
print('-' * 30)
for i, n in enumerate(ficha):
    print(f'{i:<8}{n[0]:<15}{n[2]:>3.1f}')
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas <= len(ficha) - 1:
        print(f'As notas de {ficha[notas][0]} são {ficha[notas][1]}.')
    if notas == 999:
        print('FINALIZANDO...')
        break
print('Volte sempre.')
