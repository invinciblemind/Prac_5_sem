lst = input().split()
match lst:
    case ['mov', r1, r2]:
        print(f'moving {r2} to {r1}')
    case ['push' | 'pop' as cmd, *reglst]:
        print(f'{cmd}ing {" ".join(reglst)}')
    case (0, *tail):
        print('zero tuple', tail)
    case [cmd, r1]:
        print(f'making {cmd} with {r1}')
    case _:
        print('Parse error')
