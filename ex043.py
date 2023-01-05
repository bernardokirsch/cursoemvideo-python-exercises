weight = float(input('Qual é seu peso? (Kg)'))
height = float(input('Qual é sua altura? (m)'))
imc = weight / (height) ** 2

print(f'O IMC dessa pessoa é de {round(imc, 2)}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc <= 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL!')
elif imc <= 30:
    print('Você está em SOBREPESO!')
elif imc <= 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')