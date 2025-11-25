class Doubeleton(type):
    _instance = []
    _idx = 1
    def __call__(cls, *args, **kw):
        if len(cls._instance) < 2:
             cls._instance.append(super().__call__(*args, **kw))
        cls._idx = 1 - cls._idx
        return cls._instance[cls._idx]

class C(metaclass=Doubeleton): pass
print(*(C() for i in range(7)), sep="\n")
