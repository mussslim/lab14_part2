import asyncio
import time

def fetch_sync(name, delay):
    print(f"Sync request: {name}")
    time.sleep(delay)
    return name

async def fetch_async(name, delay):
    print(f"Async request: {name}")
    await asyncio.sleep(delay)
    return name

async def main_async():
    results = await asyncio.gather(
        fetch_async("API", 2),
        fetch_async("DB", 3),
        fetch_async("File", 1),
    )
    print("Async results:", results)

if __name__ == "__main__":
    t0 = time.time()
    fetch_sync("API", 2)
    fetch_sync("DB", 3)
    fetch_sync("File", 1)
    print("Sync time:", time.time() - t0)

    t1 = time.time()
    asyncio.run(main_async())
    print("Async time:", time.time() - t1)
