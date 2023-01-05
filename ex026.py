phrase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece {phrase.count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {phrase.index("a") + 1}')
print(f'A última letra A apareceu na posição {phrase.rindex("a") + 1}')