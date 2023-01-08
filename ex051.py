print('=' * 23)
print('  10 TERMOS DE UMA PA  ')
print('=' * 23)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for i in range(n, (n + (10 - 1) * r) + 1, r):
    print(i, end=' → ')
print('ACABOU!')