print('     GERADOR DE PA     ')
print('=' * 23)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 10
count = 0

while i != 0:
    while i != 0:
        print(n, end=' → ')
        n = n + r
        i -= 1
        count += 1
    print('PAUSA!')
    i = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {count} termos mostrados.')