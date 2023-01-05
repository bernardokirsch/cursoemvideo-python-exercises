number = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))

if op == 1:
    print(f'{number} convertido para BINÁRIO é igual a {bin(number)[2:]}') #0b
elif op == 2:
    print(f'{number} convertido para OCTAL é igual a {oct(number)[2:]}') #0o
elif op == 3:
    print(f'{number} convertido para HEXADECIMAL é igual a {hex(number)[2:]}') #0x
else: 
    print('Opção inválida!')