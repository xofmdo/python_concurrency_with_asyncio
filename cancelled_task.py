import asyncio
from asyncio import CancelledError
from utils import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print(f'Задача не закончилась, следующая проверка через секунду. '
              f'Идет {seconds_elapsed} секунда')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()

        # Вызов cancel не прерывает задачу, делающую свое дело; он снимает ее,
        # только если она уже находится в точке ожидания или когда дойдет до
        # следующей такой точки.

    try:
        await long_task
    except CancelledError:
        print('Наша задача была снята')


asyncio.run(main())

# Задача не закончилась, следующая проверка через секунду. Идет 0 секунда
# засыпаю на 10 с
# Задача не закончилась, следующая проверка через секунду. Идет 1 секунда
# Задача не закончилась, следующая проверка через секунду. Идет 2 секунда
# Задача не закончилась, следующая проверка через секунду. Идет 3 секунда
# Задача не закончилась, следующая проверка через секунду. Идет 4 секунда
# Задача не закончилась, следующая проверка через секунду. Идет 5 секунда
# Наша задача была снята
