class cnst:
    frst, scnd, thrd = '', '', ''

cnst.frst, cnst.scnd, cnst.thrd = input().split()

while strk := input():
    match strk.split():
        case lst if lst[0] == cnst.frst and 'yes' in lst:
            print('word 1, yes')
        case [cnst.scnd]:
            print('scnd')
        case lst if lst[0] == cnst.thrd and lst[-1] == cnst.scnd:
            print('3...2')
