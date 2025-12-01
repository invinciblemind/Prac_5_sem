import sys
import math

b = sys.stdin.readlines()
labels = []
real_labels = set()
req_labels = set()
dct = {}
cmd = []
for strk in b:
    buf = strk.split()
    match buf:
        case [name, *other]:
            match name.split(':'):
                case [label, '']:
                    labels.append(label)
                    real_labels.add(label)
                    buf = buf[1:]
                case _:
                    labels.append('')
        case _:
            labels.append('')
        
    match buf:
        case ['stop']:
            cmd.append(buf)
        case ['store', n, str(name)]:
            try:
                cmd.append(['store', float(n), name])
                dct[name] = 0
            except Exception:
                cmd.append(['store', 0, name])
                dct[name] = 0
        case ['add' | 'sub' | 'div' | 'mul' as op, str(name1), str(name2), str(name3)]:
            cmd.append([op, name1, name2, name3])
            dct[name1] = 0
            dct[name2] = 0
            dct[name3] = 0
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as cmp, str(name1), str(name2), str(label)]:
            req_labels.add(label)
            cmd.append([cmp, name1, name2, label])
            dct[name1] = 0
            dct[name2] = 0
        case ['out', str(name1)]:
            cmd.append(buf)
            dct[name1] = 0
        case _:
            cmd.append('')
req_labels -= real_labels
i = 0
while not len(req_labels) and i < len(cmd):
    match cmd[i]:
        case ['stop']:
            break
        case ['store', n, str(name)]:
            try:
                dct[name] = float(n)
            except Exception:
                dct[name] = 0
            i += 1
        case ['add', str(name1), str(name2), str(name3)]:
            dct[name3] = dct[name1] + dct[name2]
            i += 1
        case ['sub', str(name1), str(name2), str(name3)]:
            dct[name3] = dct[name1] - dct[name2]
            i += 1
        case ['mul', str(name1), str(name2), str(name3)]:
            dct[name3] = dct[name1] * dct[name2]
            i += 1
        case ['div', str(name1), str(name2), str(name3)]:
            match dct[name2]:
                case 0:
                    dct[name3] = math.inf
                case _:
                    dct[name3] = dct[name1] / dct[name2]
            i += 1
        case ['ifeq', str(name1), str(name2), str(label)]:
            match dct[name1] == dct[name2]:
                case 1:
                    i = labels.index(label)
                case _:
                    i += 1
        case ['ifne', str(name1), str(name2), str(label)]:
            match dct[name1] != dct[name2]:
                case 1:
                    i = labels.index(label)
                case _:
                    i += 1
        case ['ifgt', str(name1), str(name2), str(label)]:
            match dct[name1] > dct[name2]:
                case 1:
                    i = labels.index(label)
                case _:
                    i += 1
        case ['ifge', str(name1), str(name2), str(label)]:
            match dct[name1] >= dct[name2]:
                case 1:
                    i = labels.index(label)
                case _:
                    i += 1
        case ['iflt', str(name1), str(name2), str(label)]:
            match dct[name1] < dct[name2]:
                case 1:
                    i = labels.index(label)
                case _:
                    i += 1
        case ['ifle', str(name1), str(name2), str(label)]:
            match dct[name1] <= dct[name2]:
                case 1:
                    i = labels.index(label)
                case _:
                    i += 1
        case ['out', str(name1)]:
            print(dct[name1])
            i += 1
        case _:
            i += 1
