import requests

request = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')

request_dict = request.json()

dolar = float(request_dict['USDBRL']['bid'])

money = float(input('Quanto dinheiro você tem na carteira? R$'))

print(f'Com R${money} você pode comprar US${round(money / dolar, 2)}')
