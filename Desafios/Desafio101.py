def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

#Programa Principal
ano = int(input('Ano de Nascimento: '))
print(voto(ano))