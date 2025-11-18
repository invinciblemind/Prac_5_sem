import random
import struct

with open('file5', 'bw+') as f:
    seq = [(random.random(), bytes(random.sample(range(5),3)), random.randrange(10000)) for i in range(10)]
    for i in seq:
        b = struct.pack('f3si', *i)
        f.write(b)

with open('file5', 'br') as f:
    with open('file6', 'bw+') as f2:
        size = f.seek(0, 2)
        f.seek(0)
        while s := f.read(size // 10):
            w = f2.write(struct.pack('!f3si', *struct.unpack('f3si', s)))
