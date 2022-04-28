import asyncio
from datetime import datetime


def log_start_end_time(func):
    def wrapper():
        print(datetime.now())

        func()

        print(datetime.now())

    return wrapper


def log_func_with_args(func):
    def wrapper(content):
        print(datetime.now())

        func(content)

        print(datetime.now())

    return wrapper
