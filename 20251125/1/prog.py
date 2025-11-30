class dump(type):
    def __new__(metacls, name, parents, ns, **kwds):
        def newf(name0, fun):
            def f(self, *args, **kwargs):
                print(f'{name0}: {args}, {kwargs}')
                return fun(self, *args, **kwargs)
            
            return f
        ns2 = {}
        for name1, f1 in ns.items():
            if callable(f1):
                ns2[name1] = newf(name1, f1)
            else:
                ns2[name1] = f1
        ns = ns2
        return super().__new__(metacls, name, parents, ns)

import sys
exec(sys.stdin.read())
