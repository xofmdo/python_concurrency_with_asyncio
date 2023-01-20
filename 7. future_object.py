from asyncio import Future
import asyncio


def make_request() -> Future:
    future = Future()
    # Создаем задачу, которая асинхронно установит значение future
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main():
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    # Приостановить main, пока значение future не установлено
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())

