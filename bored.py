import asyncio

async def make_greeting(name):
    return f'Hello {name}'
async def main():
    for name in ['Paula', 'Thomas', 'Lewis']:
        a = await make_greeting(name)
        print(a)
# Run it. Will see greetings for Paula, Thomas, and Lewis
asyncio.run(main())
