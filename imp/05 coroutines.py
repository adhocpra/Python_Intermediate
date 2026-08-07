import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(1)
    print("Taks 2 completed")

async def main():
    await task1 ()
    await task2 ()

asyncio.run(main())

#this automatically doesn't run the fastest function --> total time= 3 sec
#Asyncio Gather


async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(1)
    print("Taks 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())  

#----> total time =2 sec