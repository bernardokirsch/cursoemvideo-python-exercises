n = 0
soma = 0
count = 0
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {count - 1} números e a soma entre eles foi {soma}')