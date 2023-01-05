from datetime import datetime

year = int(input('Ano de nascimento: '))

year_now = datetime.now().year

print(f'Quem nasceu em {year} tem {year_now - year} ano(s) em {year_now}')

if year_now - year < 18:
    print(f'Ainda faltam {18 - (year_now - year)} ano(s) para o alistamento \n'
          f'Seu alistamento será em {year_now + (18 - (year_now - year))}')
elif year_now - year == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado há {(year_now - year) - 18} ano(s) \n'
          f'Seu alistamento foi em {year_now - ((year_now - year) - 18)}')