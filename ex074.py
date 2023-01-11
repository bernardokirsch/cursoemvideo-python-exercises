from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {numbers}')
print(f'O maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')