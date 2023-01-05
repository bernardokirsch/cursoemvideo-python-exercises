n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print(f'Tirando {n1} e {n2}, a média do aluno é {round((n1 + n2) / 2, 1)}')
if (n1 + n2) / 2 >= 7:
    print('O aluno está APROVADO.')
elif (n1 + n2) / 2 >= 5 and (n1 + n2) / 2 < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')