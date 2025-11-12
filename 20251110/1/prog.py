from collections import UserString

class DivStr(UserString):
    def __init__(self, s = ''):
        super().__init__(s)
    
    def __floordiv__(self, n):
        return iter([self[i * (len(self) // n):(i + 1) * (len(self) // n)] for i in range(n)])
    
    def __mod__(self, n):
        return self[len(''.join(list(map(str, self // n)))):]


import sys
exec(sys.stdin.read())
