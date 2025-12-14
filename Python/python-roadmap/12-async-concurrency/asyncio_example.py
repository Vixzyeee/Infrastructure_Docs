# asyncio_example.py
# Concurrent asyncio example using gather

import asyncio

async def task(name, delay):
    print(f"Task {name} start")
    await asyncio.sleep(delay)
    print(f"Task {name} end")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )

asyncio.run(main())
