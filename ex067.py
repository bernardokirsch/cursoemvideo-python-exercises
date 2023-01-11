number = 0
while number >= 0:
    number = int(input('Digite um número para ver sua tabuada: '))
    if number < 0:
        break
    print('-' * 12)
    for i in range(10):
        print(f'{number} x {i + 1} = {number * (i + 1)}')
    print('-' * 12)
print('-' * 12)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')