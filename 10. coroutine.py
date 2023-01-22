from collections import deque


def tick():
    for _ in range(10):
        print('Tick')
        yield


def tock():
    for _ in range(10):
        print('Tock')
        yield


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
        self.scheduler = scheduler
        self.schedule()

    def step(self):
        try:
            next(self.coroutine)
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
