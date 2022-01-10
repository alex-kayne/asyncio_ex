# event loop берет из очереди первую задачу task (наследуемый класс feature)
# у ассоцированной с этим экземпляром task корутиной вызывается метод step и корутина выполняет свой код
# если корутина вызывает след корутину, то делигириующая корутина приостанавливает свое выполнение и передает контроль выполнения в след корутину.
# если корутина вызывает блокирующую фнукцию, то контроль выполнения передается обратно в event loop для след таска
# если контроль выполнения передается с таска, на котром все началось, то таск продолжает работу с того момента, где все закончилось в пред запуск

# Пример: одна функция выводит числа от 0 до бесконечности, вторая функция выводит фразу

import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)




async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)



async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()
    asyncio.run(main())