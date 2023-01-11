print('=' * 23)
print('  10 TERMOS DE UMA PA  ')
print('=' * 23)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 10
while i != 0:
    print(n, end=' → ')
    n = n + r
    i -= 1
print('FIM!')