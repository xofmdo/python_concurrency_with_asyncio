import asyncio

from utils import delay


async def main():
    await asyncio.sleep(1)
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

    # Это похоже на то, что происходит при вызове asyncio.run, с той разницей,
    # что оставшиеся задачи не отменяются. Если нам нужна специальная логика
    # очистки, то ее следует реализовать в finally.


def call_later():
    print("Меня вызовут в ближайшем будущем!")


async def main2():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)
    # Здесь сопрограмма main2 получает цикл событий от функции
    # asyncio.get_running_loop, и вызывает его метод call_later, который
    # принимает функцию и выполняет ее на следующей итерации цикла.

asyncio.run(main2())
