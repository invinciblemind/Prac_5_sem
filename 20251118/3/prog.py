def print_title(file):
    fb = file.read_bytes()
    if len(fb) < 44:
        print('NO')
    elif fb[:4] != b'RIFF' or fb[8:12] != b'WAVE' or fb[20] + fb[21] * 256 != 1 or fb[22] + fb[23] * 256 != 2 or fb[34] + fb[35] * 256 != 16:
        print('NO')
    else:
        print(f'Size={fb[4] + fb[5] * 256 + fb[6] * 256 ** 2 + fb[7] * 256 ** 3}, Type={fb[20] + fb[21] * 256}, Channels={fb[22] + fb[23] * 256}, Rate={fb[24] + fb[25] * 256 + fb[26] * 256 ** 2 + fb[27] * 256 ** 3}, Bits={fb[34] + fb[35] * 256}, Data size={fb[40] + fb[41] * 256 + fb[42] * 256 ** 2 + fb[43] * 256 ** 3}')

import sys
exec(sys.stdin.read())
