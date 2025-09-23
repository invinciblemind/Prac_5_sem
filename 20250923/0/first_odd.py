lst = list(map(int, input().split()))
for i in lst:
    if i % 2 == 1:
        print(i)
        break
else:
    print(lst[0])
