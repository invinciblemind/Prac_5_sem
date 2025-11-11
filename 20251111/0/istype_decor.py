def istype(typ):
    def ist(f):
        def decor(*args):
            for i in args:
                if not isinstance(i, typ):
                    raise TypeError
            return f(*args)
        return decor
    return ist


@istype(int)
def mult(a, b, c):
    return a + b + c


print(mult('1', '2', '3'))
