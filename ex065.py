numbers = []
proceed = 'Ss'
while proceed in 'Ss':
    n = int(input('Digite um número: '))
    numbers.append(n)
    proceed = str(input('Quer continuar? [S/N] ')).strip()[0]
print(f'Você digitou {len(numbers)} número(s) e a média foi {round(sum(numbers) / len(numbers), 2)}')
print(f'O maior valor foi {max(numbers)} e o menor foi {min(numbers)}')