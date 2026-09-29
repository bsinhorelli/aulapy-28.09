# 4. Dado dois valores e um sinal (+,-,* ou /), efetue o calculo correspondente. Lembre-se que em caso de divisão por zero, não há como dividir:
# ENTRADA: 20 + 3 SAÍDA 23
# ENTRADA 12 $ 4 SAÍDA : Operador inválido
# ENTRADA 34 / 0 SAÍDA: Não há divisão por zero

num1 = int(input('Digite um valor:'))
operador = input('Digite um operador (+,-,* ou /): ')
num2 = int(input('Digite outro valor:'))

match operador:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        if num2 == 0:
            print('Não há divisão por zero.')
        else:
            print(num1 / num2)
    case _:
        print('Operador inválido')