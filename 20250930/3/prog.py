from math import *


def Calc(s, t ,u):
    def uu(x):
        xn = eval(s)
        y = eval(t)
        x = xn
        return eval(u)
    
    return uu

t = eval(input())
x = eval(input())
F = Calc(*t)
print(F(x))
