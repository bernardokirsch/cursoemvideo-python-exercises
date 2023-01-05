print('=' * 9, 'LOJAS KIRSCH', '=' * 9)

price = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

op = int(input('Qual a opção? '))

if op == 1:
    print(f'Sua compra de R${round(price, 2)} vai custar R${round(price * 0.90, 2)} no final.')
elif op == 2:
    print(f'Sua compra de R${round(price, 2)} vai custar R${round(price * 0.95, 2)} no final.')
elif op == 3:
    print(f'Sua compra de R${round(price, 2)} vai custar R${round(price, 2)} no final.')
elif op == 4:
    portion = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {portion}x de R${round(price * 1.2 / portion, 2)} COM JUROS \n'
          f'Sua compra de R${round(price, 2)} vai custar R${round(price * 1.2, 2)} no final.')
else:
    print('Opção inválida!')