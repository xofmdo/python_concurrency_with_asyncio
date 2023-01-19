import asyncio
from utils import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')

    # Эта программа завершается примерно через 1 с. По истечении 1 с
    # предложение wait_for возбуждает исключение TimeoutError, которое
    # обрабатывается, проверяем была ли снята задача delay, и печатаем смс:

asyncio.run(main())

# засыпаю на 2 с
# Тайм-аут!
# Задача была снята? True
