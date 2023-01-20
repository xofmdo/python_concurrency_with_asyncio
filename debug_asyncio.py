import asyncio
from utils import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


asyncio.run(main(), debug=True)


# выполняется <function cpu_bound_work at 0x100a6ba30> с аргументами () {}
# <function cpu_bound_work at 0x100a6ba30> завершилась за 2.5509 с
# Executing <Task finished name='Task-2' coro=<cpu_bound_work() done,
# defined at /Users/** result=100000000 created at /**/python3.10/asyncio/tasks.py:337> took 2.551 seconds

async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250
    # Здесь продолжительность медленного обратного вызова уст равной 250 мс,
    # т.е. сообщение печатается, если сопрограмма работает дольше 250 мс.


asyncio.run(main(), debug=True)
