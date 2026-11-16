print('CALCULADORA EM PYTHON')

print()

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um outro valor: '))


print('[1] - Adição')
print('[2] - Subtração')
print('[3] - Multiplicação')
print('[4] - Divisão')

opcao = int(input('Alternativa: '))

if opcao == 1:
    print(f'{num1} + {num2} = {num1+num2}')

elif opcao == 2:
    print(f'{num1} + {num2} = {num1-num2}')

elif opcao == 3:
    print(f'{num1} + {num2} = {num1*num2}')

elif opcao == 4:
    print(f'{num1} + {num2} = {num1/num2}')