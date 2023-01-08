n = int(input('Digite um número: '))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
        print(f'\033[0;33m{i}\33[m', end=' ')
    else:
        print(f'\033[0;31m{i}\33[m', end=' ')
print(f'\nO número {n} foi divisível {count} vezes')
if count == 2:
    print('E por isso ele É PRIMO!')
else: 
    print('E por isso ele NÃO É PRIMO!')