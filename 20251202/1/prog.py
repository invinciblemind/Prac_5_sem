import asyncio

async def writer(q, lat):
    n = 0
    while True:
        await asyncio.sleep(lat)
        await q.put(f'{n}_{lat}')
        n += 1
        if event.is_set():
            break

async def stacker(q, st):
    while True:
        res = await q.get()
        await st.put(res)
        if event.is_set():
            break

async def reader(st, cnt, lat):
    n = 0
    while True:
        await asyncio.sleep(lat)
        res = await st.get()
        print(res)
        n += 1
        if n == cnt:
            event.set()
            break

async def main():
    lat1, lat2, lat3, cnt = eval(input())
    await asyncio.gather(writer(q, lat1), writer(q, lat2), stacker(q, st), reader(st, cnt, lat3))

q = asyncio.Queue()
st = asyncio.LifoQueue()
event = asyncio.Event()

asyncio.run(main())
