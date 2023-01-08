phrase = input('Digite uma frase: ').upper().replace(' ', '')
inverted = ''
for i in range(1, len(phrase) + 1):
    inverted = inverted + phrase[-i]
print(f'O inverso de {phrase} é {inverted}')
if phrase == inverted:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')