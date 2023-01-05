import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# print(f'A hipotenusa vai medir {round((co ** 2 + ca ** 2) ** 0.5, 2)}')
print(f'A hipotenusa vai medir {round(math.hypot(co, ca), 2)}')