green = '\033[1;32m'
red = '\033[1;31m'

print(f'{green}')

print('='*6 + ' CALCULADORA EM PYTHON ' + '='*6)

print()
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite um outro valor: '))
print()

print('='*6 + ' OPERAÇÕES ' + '='*6)
print('\n[1] - Adição')
print('[2] - Subtração')
print('[3] - Multiplicação')
print('[4] - Divisão')

opcao = int(input('\nAlternativa: '))

if opcao == 1:
    print(f'\n{num1} + {num2} = {num1+num2}')

elif opcao == 2:
    print(f'\n{num1} - {num2} = {num1-num2}')

elif opcao == 3:
    print(f'\n{num1} x {num2} = {num1*num2}')

elif opcao == 4:
    if num2 != 0:
        print(f'\n{num1} / {num2} = {num1/num2}')

    else:
        print(f'\n{red}Valor inválido{green}')