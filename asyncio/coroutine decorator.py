import asyncio
import inspect

@asyncio.coroutine
def a():
    return('ok')

inspect.isgeneratorfunction(a)

g = a()

next(g)