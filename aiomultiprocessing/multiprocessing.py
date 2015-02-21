import asyncio
from multiprocessing import Process


class AsyncProcess(Process):

    @asyncio.coroutine
    def join(self):
        while self.is_alive():
            yield from asyncio.sleep(0.001)  # Just to give up the thread; we
            # don't actually really need much here.
