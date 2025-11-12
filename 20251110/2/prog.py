class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput
    else:
        sq = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
        if sq == 0:
            raise BadTriangle
        return f'{sq:.2f}'

while True:
    try:
        print(triangleSquare(input()))
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        break
