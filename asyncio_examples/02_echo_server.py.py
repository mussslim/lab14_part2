import asyncio

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')

    data = await reader.read(1024)
    message = data.decode()

    print(f"Received from {addr}: {message}")

    writer.write(data)
    await writer.drain()

    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 9095)

    async with server:
        await server.serve_forever()

asyncio.run(main())
