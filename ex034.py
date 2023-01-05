salary = float(input('Qual é o salário do funcionário? R$'))
if salary > 1250:
    print(f'Quem ganhava R${salary:.2f} passa a ganhar R${salary * 1.10:.2f} agora.')
else:
    print(f'Quem ganhava R${salary:.2f} passa a ganhar R${salary * 1.15:.2f} agora.')