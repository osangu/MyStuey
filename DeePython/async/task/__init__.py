from datetime import datetime
import asyncio as asy


async def print_start_log(): print(datetime.now())


async def task_ex():

    task1 = asy.create_task(print_start_log())
    task2 = asy.create_task(print_start_log())

    await task1
    await task2


async def task_ex2():

    await asy.gather(print_start_log(),print_start_log())

    # task를 매개변수로 받지만,
    # coroutine 함수를 받으면 알아서 변환해 실행시켜준다.


if __name__ == '__main__':

    asy.run(task_ex())

    asy.run(task_ex2())