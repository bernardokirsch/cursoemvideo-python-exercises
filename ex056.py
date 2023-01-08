names = []
ages = []
gender = []

for i in range(4):
    print('-' * 5, f'{i + 1}ª PESSOA', '-' * 5)
    names.append(str(input('Nome: ')).strip())
    ages.append(int(input('Idade: ')))
    gender.append(str(input('Sexo [M/F]: ')).upper().strip())
print(f'A média de idade do grupo é de {round(sum(ages) / len(ages), 2)} anos')
if 'M' in gender:
    print(f'O homem mais velho tem {max(ages)} anos e se chama {names[ages.index(max(ages))]}')
else:
    print('Não foram informados homens!')
count = 0
if 'F' in gender:
    for i in range(len(gender)):
        if ages[i] < 20:
            count += 1
print(f'Ao todo são {count} mulheres com menos de 20 anos')