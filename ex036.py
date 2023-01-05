price = float(input('Valor da casa: R$'))
salary = float(input('Salário do comprador: R$'))
years = int(input('Quantos anos de financiamento? '))
 
portion = price / (years * 12)

print(f'Para pagar uma casa de R${price:.2f} em {years} anos a prestação será de R${portion:.2f}')

if portion > salary * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')