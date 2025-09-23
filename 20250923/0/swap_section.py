l1 = [i for i in range(5, 16)]
l2 = [chr(i) for i in range(ord('a'), ord('k') + 1)]
l1[4:8] = l2[-5:]
print(l1)
