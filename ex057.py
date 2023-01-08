gender = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while gender not in 'MF':
    gender = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()
print(f'Sexo {gender} registrado com sucesso')