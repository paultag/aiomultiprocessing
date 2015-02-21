from aiomultiprocessing import AsyncProcess
import asyncio
import time
import os

def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    time.sleep(5)  # Note this is blocking
    print('hello', name)

@asyncio.coroutine
def hey():
    while True:
        print("Hey")
        yield from asyncio.sleep(0.5)

@asyncio.coroutine
def fnord():
    asyncio.async(hey())  # Technically a bug; but meh.
    p = AsyncProcess(target=f, args=('bob',))
    p.start()
    yield from p.join()

def main():
    info('main line')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fnord())
    loop.close()


if __name__ == "__main__":
    main()
