class CONST:
    A = 100500

match eval(input()):
    case 'QWE':
        print('QWE!')
    case 'A' | 'B' as s:
        print('Letter', s)
    case CONST.A:
        print('StoPicot')
    case int(n) if n > 0:
        print('Positive:', n)
    case int(n):
        print('Int:', n)
    case (0, *tail):
        print('zero tuple', tail)
    case (float(n) | int(n), *tail):
        print(f'{n}-tuple', tail)
    case _:
        print('UNKNOWN')
