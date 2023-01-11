from random import randint

count = 0
print('=-' * 15)
print('  VAMOS JOGAR PAR OU ÍMPAR  ')
while True:
    print('=-' * 15)
    number = int(input('Diga um valor: '))
    odd_even = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while odd_even not in 'PIÍ':
        odd_even = str(input('Opção inválida. Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computer = randint(0, 10)
    if (number + computer) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print('-' * 30)
    print(f'Você jogou {number} e o computador jogou {computer}. Total de {number + computer} deu {result}')
    print('-' * 30)
    if odd_even in result[0]:
        print('        Você VENCEU!      ')
        print('=-' * 15)        
    else:
        print('        Você PERDEU!        ')
        print('=-' * 15)
        break
    count += 1
    print('   Vamos jogar novamente...   ')
print(f'GAME OVER! Você venceu {count} vezes.')