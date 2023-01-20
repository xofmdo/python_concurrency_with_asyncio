import asyncio
from utils import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two
    # Как видим, два вызова delay работали примерно 2 и 3 с соответственно,
    # что в сумме составляет 5 с. Заметим, однако, что сопрограмма main
    # работала всего 3 с, поскольку ожидание производилось конкурентно.

asyncio.run(main())

# выполняется <function main at 0x10502d750> с аргументами () {}
# выполняется <function delay at 0x102b83be0> с аргументами (2,) {}
# засыпаю на 2 с
# выполняется <function delay at 0x102b83be0> с аргументами (3,) {}
# засыпаю на 3 с
# сон в течение 2 с закончился
# <function delay at 0x102b83be0> завершилась за 2.0021 с
# сон в течение 3 с закончился
# <function delay at 0x102b83be0> завершилась за 3.0015 с
# <function main at 0x10502d750> завершилась за 3.0017 с