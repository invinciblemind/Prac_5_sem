import sys
import pathlib

with open(sys.argv[1], 'rb+') as file:
    print(pathlib.PosixPath(sys.argv[1]))
