import sys

with open(sys.argv[1], 'rb+') as file:
    s = file.read()
    with open(sys.argv[1], 'wb') as file2:
        file2.write(s[len(s) // 2:] + s[:len(s) // 2])
    
