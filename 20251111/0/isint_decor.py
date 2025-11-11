def isint(f):
    def decor(*args):
        for i in args:
            if type(i) != int:
                raise TypeError
        return f(*args)
    return decor


@isint
def mult(a, b, c):
    return a * b * c


print(mult(1, 2, 3))
