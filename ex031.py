distance = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prester a começar uma viagem de {distance}Km.')
if distance <= 200:
    print(f'E o preço da passagem será de R${round(distance * 0.5, 2)}')
else:
    print(f'E o preço da passagem será de R${round(distance * 0.45, 2)}')