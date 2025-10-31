class Omnibus:
    dct = {}
    
    def __setattr__(self, attr, value):
        if attr not in self.__class__.dct:
            self.__class__.dct[attr] = {self.__repr__()}
        else:
            self.__class__.dct[attr].add(self.__repr__())
   
   
    def __getattr__(self, attr):
        return len(self.__class__.dct[attr])


    def __delattr__(self, attr):
        if attr in self.__class__.dct and self.__repr__() in self.__class__.dct[attr]:
            self.__class__.dct[attr].remove(self.__repr__())


import sys
exec(sys.stdin.read())
