# https://realpython.com/async-io-python/#async-io-in-python-with-asyncio

import asyncio
import time


async def count():
    # we made this func async because we know this func may run some I/O waiting jobs
    # like sleep here
    print("One")
    # instead of time.sleep we use asyncio.sleep because in python not all func come with async await
    await asyncio.sleep(5)

    # You use the await keyword to await the execution of asyncio.sleep().
    # This gives the control back to the program’s event loop, saying: I will sleep for one second.
    # Go ahead and run something else in the meantime.

    print("Two")
    await asyncio.sleep(5)


async def main():
    # uses asyncio.gather() to run three instances of count() concurrently.
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    start = time.perf_counter()
    # use the asyncio.run() function to launch the event loop and execute main()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds")


# RuntimeWarning: coroutine 'count' was never awaited


# In contrast, time.sleep() or any other blocking call is incompatible with
# asynchronous Python code because it stops everything in its tracks for the duration of the sleep time.
# The await keyword suspends the execution of the surrounding coroutine and passes control back to the event loop.


# # -----
#  when Python encounters an await f() expression in the scope of a g() coroutine,
# await tells the event loop: suspend the execution of g() until the result of f() is returned.
# In the meantime, let something else run.
# ------------
#   async def g():
#     result = await f()  # Pause and come back to g() when f() returns ; f is some I/O bound task which takes some time and we do not want to block the code
#     return result
