import random

first = input('Primeiro aluno: ')
second = input('Segundo aluno: ')
third = input('Terceiro aluno: ')
fourth = input('Quarto aluno: ')

students = [first, second, third, fourth]

print(f'O aluno escolhido foi {random.choice(students)}')