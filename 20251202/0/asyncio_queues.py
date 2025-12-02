import asyncio

async def prod():
    for i in range(5):
        strk = f'value_{i}'
        await q1.put(strk)
        print(f"prod: put {strk} to q1")
        await asyncio.sleep(1)
        

async def mid():
    while True:
        res = await q1.get()
        print(f"mid: got {res} from q1")
        await q2.put(res)
        print(f"mid: put {res} to q2")

async def cons():
    while True:
        res = await q2.get()
        print(f"cons: got {res} from q2")

async def main():
    await asyncio.gather(prod(), mid(), cons())

q1 = asyncio.Queue()
q2 = asyncio.Queue()

asyncio.run(main())
