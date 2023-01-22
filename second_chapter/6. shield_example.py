import asyncio
from asyncio import TimeoutError

from utils import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        result = await task
        print(result)

        # хьюстон, в книге проблемы, работает все иначе, вместо этой строки:
        # <function delay at 0x10e8cf820> завершилась за 10 с
        # получаю 10


asyncio.run(main())

# засыпаю на 10 с
# Задача заняла более 5 с, скоро она закончится!
# сон в течение 10 с закончился
# 10
