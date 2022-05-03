from datetime import datetime
import asyncio as asy


async def print_start_log(): print(datetime.now())


if __name__ == '__main__':
    # call in function
    async def how_to_use1(): await print_start_log()


    # call without func
    asy.run(how_to_use1())
