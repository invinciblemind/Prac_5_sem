def Subs(a, b):
    if type(a) == list:
        res = []
        for i in a:
            if i not in b:
                res.append(i)
        return res
    elif type(a) == tuple:
        res = ()
        for i in a:
            if i not in b:
                res += (i,)
        return res
    else:
        return a - b

t = eval(input())
print(Subs(*t))
