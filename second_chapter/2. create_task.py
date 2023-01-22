import asyncio
from utils import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more
    # Каждое обращение к create_task возвращает управление немедленно,
    # поэтому до предложения await sleep_for_three мы доходим сразу же.
    # В точке, где встречается первое после создания задачи предложение await,
    # все ожидающие задачи начинают выполняться, так как await запускает
    # очередную итерацию цикла событий.

asyncio.run(main())
