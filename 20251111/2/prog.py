class Num:
    def __init__(self):
        self._value = 0
    
    def __get__(self, obj, cls):
        if obj == None or '_value' not in dir(obj):
            return self._value
        return obj._value

    def __set__(self, obj, val):
        if 'real' in dir(val):
            obj._value = val
        else:
            obj._value = len(val)

    def __delete__(self, obj):
        obj._value = None

import sys
exec(sys.stdin.read())
