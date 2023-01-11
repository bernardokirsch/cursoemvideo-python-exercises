numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = ''
while True:
    number = int(input('Digite um número entre 0 e 20: '))
    while number < 0 or number > 20:
        number = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numbers[number]}')
    c = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
    while c not in 'sn':
        c = str(input('Opção inválida. Você quer continuar? [S/N] ')).strip().lower()[0]
    if c in 'n':
        break
print('Programa encerrado!')