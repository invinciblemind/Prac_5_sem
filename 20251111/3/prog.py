class Dsc:
    def __get__(self, obj, cls):
        if obj == None:
            return False
        try:
            obj.a
            obj.e
            obj.i
            obj.o
            obj.u
            obj.y
        except AttributeError:
            return False
        return True
    
    def __set__(self, obj, val):
        pass

class Vowel:
    __slots__ = 'a', 'e', 'i', 'o', 'u', 'y'
    answer = 42
    full = Dsc()
    
    def __init__(self, a=None, e=None, i=None, o=None, u=None, y=None):
        if a != None:
            self.a = a
        if e != None:
            self.e = e
        if i != None:
            self.i = i
        if o != None:
            self.o = o
        if u != None:
            self.u = u
        if y != None:
            self.y = y
    
    def __str__(self):
        s = []
        try:
            s.append('a: ' + str(self.a))
        except AttributeError:
            pass
        try:
            s.append('e: ' + str(self.e))
        except AttributeError:
            pass
        try:
            s.append('i: ' + str(self.i))
        except AttributeError:
            pass
        try:
            s.append('o: ' + str(self.o))
        except AttributeError:
            pass
        try:
            s.append('u: ' + str(self.u))
        except AttributeError:
            pass
        try:
            s.append('y: ' + str(self.y))
        except AttributeError:
            pass
        return ': '.join(s)

import sys
exec(sys.stdin.read())
