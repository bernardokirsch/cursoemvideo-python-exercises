print('=' * 47)
print('                 BANCO KIRSCH                  ')
print('=' * 47)
banknotes = [200, 100, 50, 20, 10, 5, 2, 1]
count = [0, 0, 0, 0, 0, 0, 0]
i = 0
value = int(input('Que valor você quer sacar? R$'))
while value > 0:
    while True:
        if value >= banknotes[i]:
            count[i] += 1
            value -= banknotes[i]
        else:
            i += 1
            break
print('=' * 47)
for i in range(len(count)):
    if count[i] > 0:
        print(f'Total de {count[i]} cédula(s) de R${banknotes[i]}')
print('=' * 47)
print('Volte sempre ao BANCO KIRSCH! Tenha um bom dia!')