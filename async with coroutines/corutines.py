def corutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g # декоратор для инициалиации генератора
    return inner
def subgen():
    x = 'x vernetsy v yield'
    message = yield x
    print(f'vse ok {message}')
# cd 'C:\projects\python\learningProject\async with coroutines\'
# python -i corutines.py
# g = subgen()
# g.send(None) - должен быть отправлен всегда! Инициализация
# g.send('Vasy')
# vse ok Vasy

@corutine
def average():
    count = 0
    sum = 0
    average = None
    while True:
        try:
            x = yield average
        except StopIteration:
            print('We are done here')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)

    return average # срабатывает только при исключении
# g.throw(StopIteration) - Можно пробрасывать исключения, хз зачем
