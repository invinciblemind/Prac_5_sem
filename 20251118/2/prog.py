import sys

line = ''.join(sys.stdin.readlines())
sys.stdout.write(line.encode('latin', errors='replace').decode('CP1251', errors='replace'))
