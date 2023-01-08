import math

number = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {number}! = {number}', end='')
for i in range(number - 1, 0, -1):
    print(f' x {i}', end='')
print(f' = {math.factorial(number)}')