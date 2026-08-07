#coroutine
import asyncio


async def add(a,b):
    return a+b
print(asyncio.run(add(3,5)))




async def greet():
    print("Hello")
    await asyncio.sleep(2)
    print("Good morning")

asyncio.run(greet())

