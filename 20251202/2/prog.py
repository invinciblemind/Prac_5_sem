import asyncio
import random

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    '''
    print(A1, A2)
    print(start, middle, finish)
    print(A1[start:middle], A1[middle:finish], A2[start:finish])
    print()
    '''
    await event_in1.wait()
    await event_in2.wait()
    A2[start:finish] = sorted(A1[start:middle] + A1[middle:finish])
    event_out.set()

async def mtasks(AA):
    tasks, B = [], AA.copy()
    A = AA.copy()
    events = []
    events1 = []
    ln = 1
    for i in range((len(A) + 1) // 2 * 2):
        events1.append(asyncio.Event())
        events1[-1].set()
    events.append(events1)
    k = 0
    while ln < len(A):
        events_n = []
        # print(len(events[-1]), ln, (len(A) + ln * 2 - 1) // (ln * 2) * ln * 2)
        for i in range(0, (len(A) + ln * 2 - 1) // (ln * 2) * ln * 2, ln * 2):
            # print('i =', i)
            events_n.append(asyncio.Event())
            if k % 2 == 0:
                tasks.append(merge(A, B, i, i + ln, i + ln * 2, events[-1][i // ln], events[-1][i // ln + 1], events_n[-1]))
            else:
                tasks.append(merge(B, A, i, i + ln, i + ln * 2, events[-1][i // ln], events[-1][i // ln + 1], events_n[-1]))
        if len(events_n) % 2 == 1:
            events_n.append(asyncio.Event())
            events_n[-1].set()
        ln *= 2
        k += 1
        events.append(events_n)
    if k % 2 == 0:
        return tasks, A
    else:
        return tasks, B

import sys
exec(sys.stdin.read())
