import math

angle = float(input('Digite o ângulo que você deseja: '))

radian_angle = math.radians(angle)

print(f'O ângulo de {round(angle, 2)} tem o SENO de {round(math.sin(radian_angle), 2)}')
print(f'O ângulo de {round(angle, 2)} tem o COSSENO de {round(math.cos(radian_angle), 2)}')
print(f'O ângulo de {round(angle, 2)} tem o TANGENTE de {round(math.tan(radian_angle), 2)}')