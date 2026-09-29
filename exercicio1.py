# 1. Dado um valor numérico pelo usuário, informe o dia da semana correspondente.
# ENTRADA: 2 SAÍDA: Segunda-feira
# ENTRADA: 8 SAÍDA: Valor inválido

num = int(input('Digite um valor: '))

match num:
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case _:
        print('Valor inválido!')