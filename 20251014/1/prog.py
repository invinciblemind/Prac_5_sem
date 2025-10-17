s = input().lower()
f = ''
st = set()
for i in s:
    if i.isalpha():
        if f != '':
            st.add(f + i)
        f = i
    else:
        f = ''
print(len(st))
