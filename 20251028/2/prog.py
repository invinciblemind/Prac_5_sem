class Triangle:
    def __init__(self, dot1, dot2, dot3):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3
    
    
    def __abs__(self):
        sq = abs(self.dot1[0] * (self.dot2[1] - self.dot3[1]) + self.dot2[0] * (self.dot3[1] - self.dot1[1]) + self.dot3[0] * (self.dot1[1] - self.dot2[1])) / 2
        if sq == 0:
            return 0
        return sq
    
    
    def __bool__(self):
        return abs(self) > 0
    
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    
    def __contains__(other, self):
        if abs(self) == 0:
            return True
        if abs(other) == 0:
            return False
        x1, y1 = other.dot1
        x2, y2 = other.dot2
        x3, y3 = other.dot3
        if x2 - x1 != 0:
            k12 = (y2 - y1) / (x2 - x1)
            b12 = y1 - k12 * x1
        if x3 - x1 != 0:
            k13 = (y3 - y1) / (x3 - x1)
            b13 = y1 - k13 * x1
        if x3 - x2 != 0:
            k23 = (y3 - y2) / (x3 - x2)
            b23 = y2 - k23 * x2
        for x, y in [self.dot1, self.dot2, self.dot3]:
            if x2 - x1 != 0:
                y0 = k12 * x + b12
                if (y - y0) * (y3 - y0) < 0:
                    return False
            else:
                if (x - x1) * (x3 - x1) < 0:
                    return False
            if x3 - x1 != 0:
                y0 = k13 * x + b13
                if (y - y0) * (y2 - y0) < 0:
                    return False
            else:
                if (x - x1) * (x2 - x1) < 0:
                    return False
            if x3 - x2 != 0:
                y0 = k23 * x + b23
                if (y - y0) * (y1 - y0) < 0:
                    return False
            else:
                if (x - x2) * (x1 - x2) < 0:
                    return False
        return True
    
    
    def __and__(self, other):
        if abs(self) * abs(other) == 0:
            return False
        if self in other or other in self:
            return True
        m0 = [self.dot1, self.dot2, self.dot3, self.dot1]
        m1 = [other.dot1, other.dot2, other.dot3, other.dot1]
        for i in range(3):
            x01, y01 = m0[i]
            x02, y02 = m0[i + 1]
            for j in range(3):
                x11, y11 = m1[i]
                x12, y12 = m1[i + 1]
                if x02 - x01 != 0:
                    k0 = (y02 - y01) / (x02 - x01)
                    b0 = y01 - k0 * x01
                if x12 - x11 != 0:
                    k1 = (y12 - y11) / (x12 - x11)
                    b1 = y11 - k1 * x11
                if x02 - x01 == 0:
                    if x12 - x11 == 0:
                        if x01 != x11:
                            continue
                        if min(x11, x12) <= x01 <= max(x11, x12) or min(x11, x12) <= x02 <= max(x11, x12):
                            return True
                        continue
                    x = x01
                    y = k1 * x01 + b1
                    if min(x01, x02) <= x <= max(x01, x02) and min(x11, x12) <= x <= max(x11, x12) and min(y01, y02) <= y <= max(y01, y02) and min(y11, y12) <= y <= max(y11, y12):
                        return True
                    continue
                if x12 - x11 == 0:
                    x = x11
                    y = k0 * x11 + b0
                    if min(x01, x02) <= x <= max(x01, x02) and min(x11, x12) <= x <= max(x11, x12) and min(y01, y02) <= y <= max(y01, y02) and min(y11, y12) <= y <= max(y11, y12):
                        return True
                    continue
                if k0 == k1:
                    if b0 != b1:
                        continue
                    if min(x11, x12) <= x01 <= max(x11, x12) or min(x11, x12) <= x02 <= max(x11, x12):
                        return True
                    continue
                x = (b1 - b0) / (k0 - k1)
                y = k0 * x + b0
                if min(x01, x02) <= x <= max(x01, x02) and min(x11, x12) <= x <= max(x11, x12) and min(y01, y02) <= y <= max(y01, y02) and min(y11, y12) <= y <= max(y11, y12):
                    return True
        return False


import sys
exec(sys.stdin.read())
