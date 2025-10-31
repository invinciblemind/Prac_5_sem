def rec_search(dot0, way, dot1, dct):
        if dot0 == dot1:
            return True
        if dot0 not in dct:
            return False
        options = dct[dot0]
        if options <= way:
            return False
        for new_dot in list(options - way):
            if rec_search(new_dot, way | {new_dot}, dot1, dct):
                return True
        return False


class Maze:
    dct = {}
    
    
    def __init__(self, N):
        self.lab = [['█'] * (2 * N + 1)]
        for i in range(N):
            self.lab.append(list('█·' * N + '█'))
            self.lab.append(['█'] * (2 * N + 1))
    
    
    def __setitem__(self, idx, val):
        x0, y0, x1, y1 = idx[0], idx[1].start, idx[1].stop, idx[2]
        if x0 == x1:
            for i in range(min(y0, y1), max(y0, y1)):
                if val == '·':
                    if (x0, i) not in self.__class__.dct:
                        self.__class__.dct[(x0, i)] = {(x0, i + 1)}
                    else:
                        self.__class__.dct[(x0, i)].add((x0, i + 1))
                    if (x0, i + 1) not in self.__class__.dct:
                        self.__class__.dct[(x0, i + 1)] = {(x0, i)}
                    else:
                        self.__class__.dct[(x0, i + 1)].add((x0, i))
                else:
                    if (x0, i) in self.__class__.dct:
                        self.__class__.dct[(x0, i)] -= {(x0, i + 1)}
                    if (x0, i + 1) in self.__class__.dct:
                        self.__class__.dct[(x0, i + 1)] -= {(x0, i)}
                ind = 2 + 2 * i
                self.lab[ind][1 + 2 * x0] = val
        elif y0 == y1:
            for i in range(min(x0, x1), max(x0, x1)):
                if val == '·':
                    if (i, y0) not in self.__class__.dct:
                        self.__class__.dct[(i, y0)] = {(i + 1, y0)}
                    else:
                        self.__class__.dct[(i, y0)].add((i + 1, y0))
                    if (i + 1, y0) not in self.__class__.dct:
                        self.__class__.dct[(i + 1, y0)] = {(i, y0)}
                    else:
                        self.__class__.dct[(i + 1, y0)].add((i, y0))
                else:
                    if (i, y0) in self.__class__.dct:
                        self.__class__.dct[(i, y0)] -= {(i + 1, y0)}
                    if (i + 1, y0) in self.__class__.dct:
                        self.__class__.dct[(i + 1, y0)] -= {(i, y0)}
                ind = 2 + 2 * i
                self.lab[1 + 2 * y0][ind] = val
        return val
    
    
    def __getitem__(self, idx):
        x0, y0, x1, y1 = idx[0], idx[1].start, idx[1].stop, idx[2]
        return rec_search((x0, y0), {(x0, y0)}, (x1, y1), self.__class__.dct)
    
    
    def __str__(self):
        s = ''
        for i in self.lab:
            s += ''.join(i) + '\n'
        return s[:-1]


import sys
exec(sys.stdin.read())
