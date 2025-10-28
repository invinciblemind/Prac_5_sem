class Rectangle:
    rectcnt = 0
    
    
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.__class__.rectcnt += 1
        setattr(self, f'rect_{self.rectcnt}', self.rectcnt)
    
    
    def __str__(self):
        return f'({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}), {self.rectcnt}'
    
    
    def __abs__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)
    
    def __lt__(self, rect2):
        return abs(self) < abs(rect2)
    
    
    def __eq__(self, rect2):
        return abs(self) == abs(rect2)
    
    
    def __mul__(self, num):
        return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)
    
    __rmul__ = __mul__
    
    '''
    def __getitem__(self, idx):
        lst = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
        return lst[idx]
    '''
    
    def __iter__(self):
        lst = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
        return iter(lst)
    
    
    def __bool__(self):
        return abs(self) > 0
    
    
    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.__class__.rectcnt)
