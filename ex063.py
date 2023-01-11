print('-' * 36)
print('       Sequência de Fibonacci        ')
print('-' * 36)
n = int(input('Quantos termos você quer mostrar?'))
print('~' * 36)
n1 = 0
n2 = 1
if n == 1:
    print(f'{n1} → ', end='')
elif n >= 2:
    print(f'{n1} → {n2} → ', end='')
while n > 2:
    fib = n2 + n1
    print(f'{fib} → ', end='')
    n1 = n2
    n2 = fib
    n -= 1
print('FIM!')