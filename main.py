import asyncio

async def main():
    await asyncio.sleep(1)
    print ("Foo")

if __name__ == "__main__":
    asyncio.run(main())