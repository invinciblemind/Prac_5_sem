class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass


cnt = 0
for class1 in [A, B, C, D]:
    for class2 in [A, B, C, D]:
        if class1 == C or class2 == C:
            try:
                E = type('E', (class1, class2), {})
            except TypeError:
                continue
            else:
                print(class1, class2)
                cnt += 1
print(cnt)
