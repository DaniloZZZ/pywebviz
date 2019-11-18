import trio
from trio_websocket import serve_websocket, ConnectionClosed
from logging import getLogger
from message_gen import message_gen

log = getLogger("Websocket")

class StopServer(Exception):
    pass

async def ws_serve(addr, port, iterable_fn):
    async def server(request):

        ws = await request.accept()

        async for message in iterable_fn(message_gen(ws)):
            try:
                await ws.send_message(message)
            except ConnectionClosed:
                log.warning("Connection closed")
                break

    await serve_websocket(server, addr, port, ssl_context=None)
    log.info("Websocket terminates")

def start_server(addr, port, handler_func=print):
    log.info(f"Starting ws server at {addr}:{port}")
    try:
        trio.run(ws_serve, addr, port, handler_func)
    except ConnectionClosed as e:
        log.warning(f"Connection closed: {e}")
        return

def main():
    start_server('127.0.0.1',8000)

if __name__=='__main__':
    main()
