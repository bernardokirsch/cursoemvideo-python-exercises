velocity = float(input('Qual é a velocidade atual do carro?'))
limit = 80.0
if velocity > limit:
    traffic_ticket =  (velocity - limit) * 7.0
    print(f'MULTADO! Você excedeu o limite permitido que é de {int(limit)}Km/h \n'
          f'Você deve pagar uma multa de R${round(traffic_ticket, 2)}')
print('Tenha um bom dia! Dirija com segurança!')