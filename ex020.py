import random

first = input('Primeiro aluno: ')
second = input('Segundo aluno: ')
third = input('Terceiro aluno: ')
fourth = input('Quarto aluno: ')

students = [first, second, third, fourth]
random.shuffle(students)

print(f'A ordem de apresentação será {students}')