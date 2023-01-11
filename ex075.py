numbers = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vez(es)')
print(f'O valor 3 {f"apareceu na {numbers.index(3) + 1}ª" if numbers.count(3) > 0 else "não aparece em nenhuma"} posição')
print(f'Os valores pares digitados foram:', end=' ')
count = 0
for n in numbers:
    if n % 2 == 0: 
        print(n, end=' ')
        count += 1
if count == 0:
    print('Nenhum')