# 5. Dado um valor inteiro com os 3 ultimos digitos da placa de um carro, informar o dia do rodizio
# finais 1 ou 2 - Segunda-feira
# finais 3 ou 4 - Terça-feira
# finais 5 ou 6 - Quarta-feira
# finais 7 ou 8 - Quinta-feira
# finais 9 ou 0 - Sexta-feira

# ENTRADA: 879      SAÍDA: Sexta-feira
# ENTRADA: 321      SAÍDA: Segunda-feira

placa = int(input('Digite os três ultimos digitos da sua placa: '))
ultimo_digito = placa % 10

match ultimo_digito:
    case 1 | 2:
        print('Rodizio: Segunda-feira')
    case 3 | 4:
        print('Rodizio: Terça-feira')
    case 5 | 6:
        print('Rodizio: Quarta-feira')
    case 7 | 8:
        print('Rodizio: Quinta-feira')
    case 9 | 0:
        print('Rodizio: Sexta-feira')
    case _:
        print('Valor inválido')

