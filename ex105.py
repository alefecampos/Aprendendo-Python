def notas(*num, sit=False):
    """-> analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) indica se deve ou não adicionar a situação (BOA, RAZOÁVEL OU RUIM
    :return: dicionário com várias informações sobre a situação da turma."""
    med = sum(num) / len(num)
    hist = {'total': sum(num), 'maior': max(num), 'menor': min(num), 'media': med}
    if sit:
        if med >= 7:
            hist['situacao'] = "BOA"
        elif 7 >= med < 5:
            hist['situacao'] = "RAZOÁVEL"
        else:
            hist['situacao'] = "RUIM"
    return hist


resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)

