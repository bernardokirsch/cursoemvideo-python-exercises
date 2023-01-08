weights = []
for i in range(5):
    weight = float(input(f'Peso da {i + 1}ª pessoa: '))
    weights.append(weight)
print(f'O maior peso lido foi de {max(weights)}kg')
print(f'O menor peso lido foi de {min(weights)}kg')