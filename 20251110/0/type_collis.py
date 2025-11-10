A = type('A', (), {'__f': 123})
B = type('B', (A,), {'__f': 999})
print(dir(A))
print(dir(B))
print(A.__f)
print(B.__f)
del B.__f
print(B.__f)
