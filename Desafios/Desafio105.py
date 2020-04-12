def notas(* n, sit=False):
    """
    -> Analisa notas de alunos.
    :param n: notas do aluno
    :param sit: se quer mostrar a situação ou não
    :return: Retorna a quantidade de notas, a maior, a menor e a media
    """
    r = {}
    maior = menor = media = 0
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r



#Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)