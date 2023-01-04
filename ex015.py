number_days = int(input('Quantos dias alugado? '))
number_km = float(input('Quantos km rodados? '))

total = number_days * 60 + number_km * 0.15

print(f'O total a pagar é de R${round(total, 2)}')