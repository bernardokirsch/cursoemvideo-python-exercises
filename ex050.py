total = 0
count = 0
for i in range(0, 6):
    number = int(input(f'Digite o {i + 1}° valor: ')) 
    if number % 2 == 0:
        total += number
        count += 1
print(f'Você informou {count} número(s) PAR(ES) e a soma foi de {total}')