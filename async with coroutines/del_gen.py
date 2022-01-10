def corutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g # декоратор для инициалиации генератора
    return inner

class BlaBlaException(Exception):
    pass
@coroutine
def subgen():
    while True:
        try:
            message = yield
        except BlaBlaException:
            print('Ku-Ku!!!')
        else:
            print('.........', message)

@coroutine
def delegator(g):
    # while True: - этот весь код нужен чтобы пробрасывать в subgen сообщения
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    yield from g # а это альтернатива кода выше