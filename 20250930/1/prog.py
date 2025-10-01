def Pareto(*pairs):
    m = []
    for i in pairs:
        for j in pairs:
            if i[0] < j[0] and i[1] <= j[1] or i[0] <= j[0] and i[1] < j[1]:
                break
        else:
            m.append(i)
    return tuple(m)

t = eval(input())
print(Pareto(*t))
