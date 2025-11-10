def div(a, b, eps):
    if abs(b) < abs(eps):
        raise ZeroDivisionError
    return a / b

print(div(5, 2, 1))
print(div(5, 0.01, 0.1))
