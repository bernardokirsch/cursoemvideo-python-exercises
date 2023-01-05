print('-=' * 15)
print('-= Analisador de Triângulos =-')
print('-=' * 15)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    if seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
    elif seg1 == seg2 and seg1 == seg3 and seg2 == seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')