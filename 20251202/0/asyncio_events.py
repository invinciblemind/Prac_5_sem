import asyncio

async def snd():
    evsnd.set()
    print(f'snd: generated evsnd')

async def mid(k):
    await evsnd.wait()
    print(f'mid{k}: received evsnd')
    if k:
        evmid1.set()
        print(f'mid: generated evmid1')
    else:
        evmid0.set()
        print(f'mid: generated evmid0')

async def rcv():
    await evmid0.wait()
    print(f'rcv: received evmid0')
    await evmid1.wait()
    print(f'rcv: received evmid1')

async def main():
    tasks = await asyncio.gather(rcv(), mid(1), mid(0), snd())

evsnd = asyncio.Event()
evmid0 = asyncio.Event()
evmid1 = asyncio.Event()
evrcv = asyncio.Event()

asyncio.run(main())
