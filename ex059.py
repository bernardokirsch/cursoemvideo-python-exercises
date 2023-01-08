n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op != 5: 
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
    ''')
    
    op = int(input('Qual é a sua opção?'))
    print('\n', end='')
    print('-=' * 20)
    
    if op == 1:
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação de {n1} x {n2} é {n1 * n2}')
    elif op == 3:
        numbers = [n1, n2]
        print(f'O maior número entre {n1} e {n2} é {max(numbers)}')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Saindo do programa...')
        print('Programa encerrado!')
        print('-=' * 20)
        break
    else:
        print('Opção inválida. Tente novamente!')
    print('-=' * 20)