import random

# from random import randint
# numberComputer = randint(1, 5)

start = 1
final = 100
numbers = list(range(start, final + 1))
numberComputer = random.choice(numbers)
print('-=-' * 20)
print(f'Vou pensar em um número entre {numbers[0]} e {numbers[-1]}. Tente adivinhar...')
print('-=-' * 20)
numberUser = int(input('Em que número pensei? '))
print('PROCESSANDO...')
if numberComputer == numberUser:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else: 
    print(f'GANHEI! Eu pensei no número {numberComputer} e não no {numberUser}!')