total = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        total += i
        count += 1
print(f'A soma de todos os {count} valores solicitados é {total}')