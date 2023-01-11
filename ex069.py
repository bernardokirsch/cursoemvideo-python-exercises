count = count1 = count2 = 0
ages = []
genres = []
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA     ')
    print('-' * 30)
    ages.append(int(input('Idade: ')))
    gender = str(input('Sexo: [M/F] ')).strip().lower()[0]
    while gender not in 'mf':
        gender = str(input('Sexo: [M/F] ')).strip().lower()[0]
    genres.append(gender)
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if op not in 'Ss':
        break
for i in range(len(ages)):
    if ages[i] >= 18:
        count += 1
    if genres[i] in 'Mm':
        count1 += 1
    if genres[i] in 'Ff' and ages[i] < 20:
        count2 += 1
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {count}')
print(f'Ao todo temos {count1} homem(ns) cadastrados')
print(f'E temos {count2} mulher(es) com menos de 20 anos')