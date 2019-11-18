from ws_server import start_server, StopServer
from ws_client import start_client
from multiprocessing import Process

def test_simple():
    async def server(message_gen):
        yield 'hello,'
        yield 'Ms. Client'
        async for message in message_gen:
            print('<<',message)
            #Listen only for one message
            raise StopServer()

    p = Process(target=start_server,
                args=('localhost', 8000, server)
               )
    p.start()

    received = []
    async def client(message_gen):
        async for message in message_gen:
            print(">>"+message)
            received.append(message)
            yield 'Hi, Server'

        # Test if sending when connection ended
        while True:
            yield 'knock'
    start_client('ws://localhost:8000', client)

    assert received[0] == 'hello,'

