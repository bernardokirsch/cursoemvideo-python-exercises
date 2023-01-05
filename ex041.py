from datetime import datetime

year = int(input('Ano de Nascimento:'))
year_now = datetime.now().year

print(f'O atleta tem {year_now - year} anos')

if year_now - year <= 9:
    print('Classificação: MIRIM')
elif year_now - year > 9 and year_now - year <= 14:
    print('Classificação: INFANTIL')
elif year_now - year > 14 and year_now - year <= 19:
    print('Classificação: JÚNIOR')
elif year_now - year > 19 and year_now - year <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')