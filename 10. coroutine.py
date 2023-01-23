from collections import deque
from time import time


def sleep(delay=0):
    d = time() + delay
    while True:
        yield
        if d <= time():
            break


def coroutine():
    result = 0
    for number in range(10):
        result += number
        print('Now yielding!')
        yield
    return result


def tick():
    result = yield from coroutine()
    print(result)


def tock():
    for _ in range(10):
        print('Tock')
        yield sleep(2)


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add(self, callback):
        self.queue.append(callback)

    def run(self):
        while self.queue:
            callback = self.queue.popleft()
            callback()

    def create_task(self, coroutine):
        task = Task(coroutine, self)
        return task


class Task:
    def __init__(self, coroutine, scheduler):
        self.coroutine = coroutine
        self.stack = []
        self.scheduler = scheduler
        self.schedule()

    def step(self):
        try:
            self.coroutine.send(None)
        except StopIteration:
            pass
        else:
            self.schedule()

    def schedule(self):
        self.scheduler.add(self.step)


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.create_task(tick())
    scheduler.create_task(tock())
    scheduler.run()


# https://www.youtube.com/watch?v=_obr60qv6rM&t=824s
# разбор материалов по теме корутины
