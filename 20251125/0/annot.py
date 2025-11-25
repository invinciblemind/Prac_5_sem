import inspect

class C:
    a: int
    def __init__(self, val):
        if type(val) == inspect.get_annotations(self.__class__)['a']:
            self.a = val
