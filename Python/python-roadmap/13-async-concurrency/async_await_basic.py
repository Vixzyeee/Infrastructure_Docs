# async_await_basic.py
# Basic async / await example

import asyncio

async def say_hello(name):
    print(f"Hello {name} - start")
    await asyncio.sleep(1)
    print(f"Hello {name} - end")

async def main():
    await say_hello("Pito")
    await say_hello("Alex")

asyncio.run(main())
