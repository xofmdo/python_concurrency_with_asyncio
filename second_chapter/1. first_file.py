import asyncio
from utils import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    # await блокирует выполнение, т.е. мы приостанавливаем всю сопрограмму на
    # время, пока выражение await не вернет управление.
    print(one_plus_one)
    print(message)

asyncio.run(main())
