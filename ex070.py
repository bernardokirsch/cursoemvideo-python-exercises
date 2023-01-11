count = 0
items = []
prices = []
print('-' * 28)
print('     LOJA SUPER KIRSCH     ')
print('-' * 28)
while True:
    items.append(str(input('Nome do Produto: ')).strip())
    prices.append(int(input('Preço: R$')))
    op = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while op not in 'sn':
        op = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().lower()[0]
    if op not in 's':
        break
    print('-' * 28)
for i in range(len(prices)):
    if prices[i] >= 1000:
        count += 1
print('-' * 6, 'FIM DO PROGRAMA', '-' * 6)
print(f'O total da compra foi R${sum(prices):.2f}')
print(f'Temos {count} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {items[prices.index(min(prices))]} que custa R${min(prices):.2f}')