digito  = input('Digite um caracter: ')

match digito:
    case 0|1|2|3|4|5|6|7|8|9:
        print('Número')
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('Vogal minúscula')
    case 'A' | 'E' | 'I' | 'O' | 'U':
        print('Vogal maiúscula')
    case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'y'|'z':
        print('Consoante minúscula')
    case 'B'|'C'|'D'|'F'|'G'|'H'|'J'|'K'|'L'|'M'|'N'|'P'|'Q'|'R'|'S'|'T'|'V'|'W'|'X'|'Y'|'Z':
        print('Consoante maiúscula')
    case _:
        print('Caracter especial')
        