def objcount(cls):
    class New(cls):
        counter = 0
        def __init__(self, *args):
            super().__init__(*args)
            New.counter += 1
        
        def __del__(self):
            if '__del__' in dir(cls):
                super().__del__()
            New.counter -= 1
    
    return New

import sys
exec(sys.stdin.read())
