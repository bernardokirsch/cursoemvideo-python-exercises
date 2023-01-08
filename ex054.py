from datetime import datetime

year_now = datetime.now().year
larger = 0
smaller = 0

for i in range(7):
    year = int(input(f'Em que ano a {i + 1}ª pessoa nasceu?'))
    if year <= year_now - 18:
        larger += 1
    else:
        smaller += 1
print(f'Ao todo tivemos {larger} pessoas maiores de idade \n'
      f'E também tivemos {smaller} pessoas menores de idade')