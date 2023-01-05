name = str(input('Qual seu nome completo? ')).strip().lower().split()
# print('Seu nome tem Silva?', 'silva' in name)
silva = False
for i in range(len(name)):
    if name[i] == 'silva':
        silva = True
print('Seu nome tem Silva?', silva)