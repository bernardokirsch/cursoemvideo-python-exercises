from random import randint
import time

count = 0
numberComputer = randint(0, 10)
numberUser = 11

print('-=-' * 20)
print(f'  Vou pensar em um número entre 0 e 10. Tente adivinhar...  ')
print('---' * 20)
print('         Será que você consegue adivinhar qual foi?          ')
print('-=-' * 20)

while numberUser != numberComputer:
    numberUser = int(input('Qual seu palpite? '))
    count += 1
    if numberComputer == numberUser:
        print(f'Acertou com {count} tentativa(s). Parabéns!')
    elif numberComputer > numberUser: 
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')