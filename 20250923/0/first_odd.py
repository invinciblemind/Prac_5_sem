lst = eval(input())
for i in lst:
    if i % 2 == 1:
        print(i)
        break
else:
    print(lst[0])
