class Counter:
    cnt = 0
    
    def __get__(self, obj, cls):
        return self.__class__.cnt

    def __set__(self, obj, val):
        self.__class__.cnt = val


class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1

c = C()
print(c.counter)
d = C()
print(d.counter)
del c
print(d.counter)
