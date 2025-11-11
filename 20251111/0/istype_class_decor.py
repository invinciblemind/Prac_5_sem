class istype:
    def __init__(self, typ):
        self.typ = typ
    
    def __call__(self, f):
        def decor(*args):
            for i in args:
                if not isinstance(i, self.typ):
                    raise TypeError
            return f(*args)
        return decor


def istype_sec(typ):
    class Dec:
        def __init__(self, f):
            self.f = f
        
        def __call__(self, *args):
            for i in args:
                if not isinstance(i, typ):
                    raise TypeError
            return self.f(*args)
    return Dec


@istype(str)
def mult(a, b, c):
    return a + b + c


@istype_sec(str)
def mult2(a, b, c):
    return a + b + c


print(mult('1', '2', '3'))
print(mult2('1', '2', '3'))
