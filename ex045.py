from random import randint
import time

choices = ['PEDRA', 'PAPEL','TESOURA']

computer = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada?'))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-=' * 8)
print(f'Computador jogou {choices[computer]}')
print(f'Jogador jogou {choices[player]}')
print('-=' * 8)

if player == 1:
    if player == computer:
        print('EMPATE!')
    elif computer == 3:
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
elif player == 2:
    if player == computer:
        print('EMPATE!')
    elif computer == 1:
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
elif player == 3:
    if player == computer:
        print('EMPATE!')
    elif computer == 2:
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCE!')
else:
    print('Opção inválida!')