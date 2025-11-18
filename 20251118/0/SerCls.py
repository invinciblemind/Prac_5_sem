import pickle

class SerCls:
    lst = [1, 2, 3]
    dct = {'1': 1, '2': 2}
    num = 123
    st = 'abc'

ser = SerCls()
t = pickle.dumps(ser)
del ser
'''
del SerCls

class SerCls:
    lst = 'qqwe'
    dct = 1234
    num = ()
    st = [1, 1, 1]

class SerCls:
    lst = []
    dct = {}
    num = 0
    st = ''

class SerCls:
    pass
'''
ser1 = pickle.loads(t)
print(ser1.lst, ser1.dct, ser1.num, ser1.st)
