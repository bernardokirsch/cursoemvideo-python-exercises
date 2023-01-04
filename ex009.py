number = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for i in range(10):
    print(f'{number} x {i + 1} = {number * (i + 1)}')
print('-' * 12)