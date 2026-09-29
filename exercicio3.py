# 3. Dada uma letra pelo usuário, informar se ela é vogal ou consoante

letra = input('Digite uma letra: ').lower()

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('Vogal')
    case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'y'|'z':
        print('Consoante')
    case _:
        print('Não é letra!')